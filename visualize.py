import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import os
from analysis import analyze_results

# Set up the matplotlib style
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica', 'Arial', 'DejaVu Sans', 'sans-serif'],
    'font.size': 12,
    'axes.titlesize': 24,
    'axes.labelsize': 20,
    'xtick.labelsize': 18,
    'ytick.labelsize': 20,
    'legend.fontsize': 20,
    'figure.titlesize': 24,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.format': 'pdf',
    'savefig.bbox': 'tight',
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
})

# ColorBrewer color palettes
COLOR_PALETTE_1 = sns.color_palette("Set2", 3)
COLOR_PALETTE_2 = sns.color_palette("Set3", 4)

# Hardcoded model order
MODEL_ORDER = ['gpt-3.5-turbo', 'gpt-4o', 'claude-sonnet-3.5']

def prepare_data(individual_results):
    data = []
    for settings, summary in individual_results:
        model = settings['model']
        if 'claude' in model.lower():
            model = 'claude-sonnet-3.5'
        data.append({
            'assignment': settings['input_dir'],
            'model': model,
            'prompt_file': settings['prompt_file'],
            'include_starter_code': settings['include_pdf'],
            'include_test_code': settings['include_test'],
            'pass_rate': summary['pass_rate'],
            'iteration': settings['iteration']
        })
    return pd.DataFrame(data)

def clamp_and_adjust(mean, std):
    # Clamp mean to [0, 100] range
    mean = np.clip(mean, 0, 100)
    
    # Clamp std to ensure mean ± std is within [0, 100]
    std = np.minimum(std, np.minimum(mean, 100 - mean))
    
    # If std is 0, set it to a small value (e.g., 0.5% of the mean or 0.5, whichever is larger)
    std = np.maximum(std, np.maximum(0.005 * mean, 0.5))
    
    return mean, std

def plot_assignment_difficulty(df):
    df_filtered = df[
        (df['include_starter_code'] == True) &
        (df['include_test_code'] == True)    &
        (df['prompt_file'] == 'level4.txt')
    ]
    
    stats = df_filtered.groupby(['assignment', 'model'])['pass_rate'].agg(['mean', 'std'])
    
    # Apply clamping and adjustment
    stats['mean'], stats['std'] = zip(*stats.apply(lambda row: clamp_and_adjust(row['mean'], row['std']), axis=1))
    
    # Calculate average performance across all models
    average_performance = stats.groupby(level='assignment')['mean'].mean()
    assignment_order = average_performance.sort_values(ascending=False).index
    
    fig, ax = plt.subplots(figsize=(12, 8.5))
    x = np.arange(len(assignment_order))
    width = 0.25
    
    textures = ['', '/', '.']
    
    for i, model in enumerate(MODEL_ORDER):
        model_data = stats.xs(model, level='model')
        means = model_data.loc[assignment_order, 'mean']
        stds = model_data.loc[assignment_order, 'std']
        
        bars = ax.bar(x + i*width, means, width, label=model, color=COLOR_PALETTE_1[i],
                      edgecolor='black', linewidth=1)
        ax.errorbar(x + i*width, means, yerr=stds, fmt='none', ecolor='black', capsize=3)
        
        for bar in bars:
            bar.set_hatch(textures[i])
    
    ax.set_ylabel('Pass Rate (%)')
    ax.set_title('Pass Rate for Each Model (Advanced Prompt + Including Code/Tests)')
    ax.set_xticks(x + width)
    ax.set_xticklabels(assignment_order,  ha='center')
    ax.set_ylim(0, 105)
    ax.set_yticks([0, 20, 40, 60, 80, 100])
    ax.legend(loc='upper center')
    
    plt.tight_layout()
    plt.savefig('figures/assignment_difficulty.pdf')
    plt.close()

def plot_input_comparison(df):
    # Filter by prompt file
    df_filtered = df[df['prompt_file'] == 'level4.txt']
    
    # Group the data and calculate mean and standard deviation
    stats = df_filtered.groupby(['model', 'include_starter_code', 'include_test_code'])['pass_rate'].agg(['mean', 'std'])
    
    # Apply clamping and adjustment
    stats['mean'], stats['std'] = zip(*stats.apply(lambda row: clamp_and_adjust(row['mean'], row['std']), axis=1))
    
    fig, ax = plt.subplots(figsize=(12, 8.5))
    x = np.arange(len(MODEL_ORDER))
    width = 0.2
    
    textures = ['', '/', '\\', 'O']
    
    configs = [
        ('Without Starter Code, Without Test Code', (False, False)),
        ('Without Starter Code, With Test Code', (False, True)),
        ('With Starter Code, Without Test Code', (True, False)),
        ('With Starter Code, With Test Code', (True, True))
    ]
    
    for i, (config_label, (include_starter, include_test)) in enumerate(configs):
        try:
            config_data = stats.xs((include_starter, include_test), level=['include_starter_code', 'include_test_code'])
            means = [config_data.loc[model, 'mean'] if model in config_data.index else 0 for model in MODEL_ORDER]
            stds = [config_data.loc[model, 'std'] if model in config_data.index else 0 for model in MODEL_ORDER]
            
            bars = ax.bar(x + i*width, means, width, label=config_label, color=COLOR_PALETTE_2[i],
                          edgecolor='black', linewidth=1)
            ax.errorbar(x + i*width, means, yerr=stds, fmt='none', ecolor='black', capsize=3)
            
            for bar in bars:
                bar.set_hatch(textures[i])
        except KeyError:
            print(f"No data for configuration: {config_label}")
    
    ax.set_ylabel('Pass Rate (%)')
    ax.set_title('Impact of Input Files on Model Performance')
    ax.set_xticks(x + 1.5*width)
    ax.set_xticklabels(MODEL_ORDER, ha='center')
    ax.set_ylim(0, 105)
    ax.set_yticks([0, 20, 40, 60, 80, 100])
    ax.legend(loc='upper left', bbox_to_anchor=(0.02, 0.98))
    
    plt.tight_layout()
    plt.savefig('figures/input_comparison.pdf')
    plt.close()

def plot_prompt_comparison(df):
    # Filter for cases where both starter code and test code are included
    df_filtered = df[
        (df['include_starter_code'] == True) &
        (df['include_test_code'] == True)
    ]
    
    # Group the data and calculate mean and standard deviation
    stats = df_filtered.groupby(['assignment', 'model', 'prompt_file'])['pass_rate'].agg(['mean', 'std'])
    
    # Apply clamping and adjustment
    stats['mean'], stats['std'] = zip(*stats.apply(lambda row: clamp_and_adjust(row['mean'], row['std']), axis=1))
    
    # Calculate average performance across all models and prompts
    average_performance = stats.groupby(level='assignment')['mean'].mean()
    assignment_order = average_performance.sort_values(ascending=False).index

    fig, ax = plt.subplots(figsize=(12, 4.5))
    x = np.arange(len(assignment_order))
    width = 0.15
    textures = ['', '\\', '/', '//', '.', 'o']
    prompt_files = ['level2.txt', 'level4.txt']
    prompt_labels = ['Simple', 'Advanced']
    
    for i, model in enumerate(MODEL_ORDER):
        for j, (prompt_file, prompt_label) in enumerate(zip(prompt_files, prompt_labels)):
            try:
                model_prompt_data = stats.xs((model, prompt_file), level=['model', 'prompt_file'])
                means = [model_prompt_data.loc[assignment, 'mean'] if assignment in model_prompt_data.index else 0 for assignment in assignment_order]
                stds = [model_prompt_data.loc[assignment, 'std'] if assignment in model_prompt_data.index else 0 for assignment in assignment_order]
                
                position = x + (i*2 + j)*width
                bars = ax.bar(position, means, width, label=f'{model} ({prompt_label})',
                              color=COLOR_PALETTE_1[i], alpha=0.7 if j == 0 else 1,
                              edgecolor='black', linewidth=1)
                ax.errorbar(position, means, yerr=stds, fmt='none', ecolor='black', capsize=3)
                
                for bar in bars:
                    bar.set_hatch(textures[i*2 + j])

            except KeyError:
                print(f"No data for model {model} with prompt file {prompt_file}")
    
    ax.set_ylabel('Pass Rate (%)')
    ax.set_title('Impact of Prompt Level on Model Performance Across Assignments')
    ax.set_xticks(x + 2.5*width)
    ax.set_xticklabels(assignment_order, ha='center')
    ax.set_ylim(0, 105)
    ax.set_yticks([0, 20, 40, 60, 80, 100])
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3)
    
    plt.tight_layout()
    plt.savefig('figures/prompt_comparison.pdf')
    plt.close()

def main():
    base_output_dir = "results_merged"
    individual_results = analyze_results(base_output_dir)
    df = prepare_data(individual_results)
    
    os.makedirs('figures', exist_ok=True)
    
    plot_assignment_difficulty(df)
    plot_input_comparison(df)
    plot_prompt_comparison(df)


if __name__ == "__main__":
    main()
