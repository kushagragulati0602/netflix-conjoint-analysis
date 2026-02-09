import numpy as np
import pandas as pd
import random

# Attributes for our Netflix Study
ATTRIBUTES = {
    'price': [6.99, 11.99, 15.49, 22.99],
    'ads': ['None', 'Limited', 'Standard'],
    'quality': ['720p', '1080p', '4K+HDR'],
    'screens': [1, 2, 4]
}

# Simulated "True" Part-Worth Utilities
TRUE_UTILITIES = {
    'price': {6.99: 2.5, 11.99: 1.2, 15.49: -0.5, 22.99: -2.8},
    'ads': {'None': 1.5, 'Limited': 0.2, 'Standard': -1.2},
    'quality': {'720p': -1.0, '1080p': 0.5, '4K+HDR': 1.8},
    'screens': {1: -0.5, 2: 0.3, 4: 1.2}
}

def generate_simulated_data(num_respondents=200, tasks_per_respondent=8):
    """
    Generates simulated conjoint analysis data.
    """
    dataset = []

    for r in range(num_respondents):
        for t in range(tasks_per_respondent):
            options = []
            utilities = []
            
            # Generate 3 options per task
            for opt_id in range(3):
                # Randomly select attributes
                price = random.choice(ATTRIBUTES['price'])
                ads = random.choice(ATTRIBUTES['ads'])
                quality = random.choice(ATTRIBUTES['quality'])
                screens = random.choice(ATTRIBUTES['screens'])
                
                # Calculate utility
                u = (TRUE_UTILITIES['price'][price] + 
                     TRUE_UTILITIES['ads'][ads] + 
                     TRUE_UTILITIES['quality'][quality] + 
                     TRUE_UTILITIES['screens'][screens])
                
                # Add random noise
                u += (random.random() - 0.5) * 2
                
                options.append({
                    'id': opt_id,
                    'price': price,
                    'ads': ads,
                    'quality': quality,
                    'screens': screens
                })
                utilities.append(u)
            
            # Selection (Logit rule: pick highest utility)
            chosen_index = utilities.index(max(utilities))
            
            dataset.append({
                'respondentId': r,
                'taskId': t,
                'options': options,
                'chosenIndex': chosen_index
            })
            
    return dataset

def get_chart_data():
    """
    Returns formatted data for charts based on TRUE_UTILITIES.
    """
    data = {}
    titles = {
        'price': 'Price Utility',
        'ads': 'Ad Experience',
        'quality': 'Video Quality',
        'screens': 'Device Screens'
    }
    
    for attr, values in TRUE_UTILITIES.items():
        df = pd.DataFrame(list(values.items()), columns=['name', 'value'])
        df['name'] = df['name'].astype(str) # Ensure names are strings for charts
        data[attr] = {
            'data': df,
            'title': titles[attr]
        }
        
    # Importance data (hardcoded as in original)
    data['importance'] = pd.DataFrame([
        {'name': 'Price', 'value': 45},
        {'name': 'Ads', 'value': 25},
        {'name': 'Quality', 'value': 20},
        {'name': 'Screens', 'value': 10},
    ])
    
    return data

def calculate_market_share(sim_options):
    """
    Calculates market share based on simulated options.
    """
    shares = []
    names = []
    
    for opt in sim_options:
        u = (TRUE_UTILITIES['price'][opt['price']] + 
             TRUE_UTILITIES['ads'][opt['ads']] + 
             TRUE_UTILITIES['quality'][opt['quality']] + 
             TRUE_UTILITIES['screens'][opt['screens']])
        shares.append(np.exp(u))
        names.append(opt['name'])
        
    total_share = sum(shares)
    percentages = [round((s / total_share) * 100) for s in shares]
    
    return pd.DataFrame({'name': names, 'value': percentages})
