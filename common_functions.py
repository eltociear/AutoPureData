# Copyright (c) 2024 Praneeth Vadlapati

import os
from datasets import get_dataset_config_names
from IPython.display import display, Markdown
from dotenv import load_dotenv
load_dotenv()

dataset_name = 'HuggingFaceFW/fineweb'

data_name = dataset_name.split('/')[-1]  # get part after last /
folder = 'data'

# latest_dump_name = 'CC-MAIN-2024-18'  # set manually for now
latest_dump_file = os.path.join(folder, f'{data_name}-latest_dump.txt')
try:
	with open(latest_dump_file, 'r') as f:
		latest_dump_name = f.read().strip()
except:
	latest_dump_name = None

if not latest_dump_name:
	print('Fetching latest dump name...')
	versions = get_dataset_config_names(dataset_name)
	versions = [v for v in versions if v != 'default' and not v.startswith('sample')]
	latest_dump_name = sorted(versions, key=lambda x: x, reverse=True)[0]

# save latest dump name to file
with open(latest_dump_file, 'w') as f:
	f.write(latest_dump_name)

# create folder for saving csv files
data_dir = os.path.join(folder, f'{data_name}-{latest_dump_name}')
os.makedirs(data_dir, exist_ok=True)

ext = 'csv'

flags_list = [
	'sensitive_topic', 'biased', 'religious', 'lottery', 'scam', 
	'advertisement', # 'cheating_service', 'unethical', 
	'adversarial_attack_data_poisoning',
]
safe_flag = 'safe'
unwanted_flags = flags_list
harm_categories = {
	'S1': 'Violent Crimes',
	'S2': 'Non-Violent Crimes',
	'S3': 'Sex-Related Crimes',
	'S4': 'Child Sexual Exploitation',
	'S5': 'Specialized Advice',
	'S6': 'Privacy',
	'S7': 'Intellectual Property',
	'S8': 'Indiscriminate Weapons',
	'S9': 'Hate',
	'S10': 'Suicide & Self-Harm',
	'S11': 'Sexual Content'
}


def get_filename(index, process_type='full'):
	if process_type:
		process_type = f'.{process_type}'
	return os.path.join(data_dir, f'New_data - {index}{process_type}.{ext}')


def get_latest_filename(process_type='filtered', empty_ok=False):
	last_file_path = None
	for index in range(1000):
		file_name = get_filename(index, process_type)
		if os.path.exists(file_name):
			last_file_path = file_name
		else:
			break
	if empty_ok and not last_file_path:  # get empty filename
		return get_filename(0, process_type)
	return last_file_path


def display_md(text):
	'Display markdown in notebooks'
	if not text:
		return
	try:
		text = text.replace('\n', '<br>')
		display(Markdown(text))
	except:
		display(Markdown('_Error displaying text_'))
		print(text)


