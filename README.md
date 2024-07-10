<!-- Copyright (c) 2024 Praneeth Vadlapati -->

# <img src="./files/logo_small.png" align="left" width="200" alt="AutoPureData" /> Auto *Pure* Data
<!-- # $${\color{darkgreen}title here}$$ -->
<!-- # <span style="color: darkgreen; font-family: 'Segoe UI'; font-size: 48px;">title here</span> -->

Automated Filtering of Unwanted Web Data to Update LLM Knowledge

[![License: AFL v3](https://img.shields.io/badge/License-AFLv3-yellow.svg?style=for-the-badge)](./LICENSE.md)
[![arxiv 2406.19271](https://img.shields.io/badge/arXiv-2406.19271-B31B1B?logo=arxiv&style=for-the-badge)](https://arxiv.org/abs/2406.19271)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)

[![Hits](https://hits.sh/github.com/Pro-GenAI/AutoPureData/hits.svg?view=today-total&style=for-the-badge&label=views&color=2a8f05&logo=github)](https://hits.sh/github.com/Pro-GenAI/AutoPureData/hits/)
![GitHub stars](https://img.shields.io/github/stars/Pro-GenAI/AutoPureData?style=for-the-badge&logo=github)

Created by Praneeth Vadlapati ([@prane-eth](https://github.com/prane-eth))

> [!NOTE]
> Please star :star: the repository to show your support. <br>

#### Why AutoPureData?
LLMs (Generative AI) like ChatGPT do not have the latest updated information.
The reason for not auto-updating with the latest data is a lot of unsafe or unwanted text around the web.

This project is to automatically collect the data and filter unwanted text using AI and LLMs.
The auto-filtered data can be used to automatically update knowledge of LLMs.


#### _What are filtered:_
- **Unsafe content** :biohazard:: Toxic, threat, insult, discrimination, political, self-harm,
	religious, violence, sexual, profanity, flirtation, spam, scam, misleading, and more
- **Content from unreliable sources** :newspaper:: Unsafe websites and unindexed domains (that are not crawled by search engines)
- **Peronal details** :bust_in_silhouette:: Phone, address, credit card, SSN, IP address, and more
- **Attacks** :shield:: Adversarial attack attempts (with Data Poisoning)

Languages supported: Only English for now (more languages will be added when contributors are available)


## :rocket: Quick Start
```bash
cp .env.example .env
pip install -r requirements.txt
```
Now, edit the `.env` file and add your API keys. <br>
Run the file [Data_filtering.ipynb](./Data_filtering.ipynb)
	to collect and filter the latest web data.

The collected data can be used for automated fine-tuning of LLMs in [this way](https://platform.openai.com/docs/guides/fine-tuning).

After the filtering process, the data can be used with an LLM as mentioned in [Usage_with_LLMs.ipynb](Usage_with_LLMs.ipynb)


## :hammer_and_wrench: Contributing
The code has a lot of room for improvement and is still in progress. <br>
Contributions are welcome! Feel free to create an issue for any bug reports or suggestions. <br>
Please contribute to the code by adding more filters and making the code more efficient. <br>
To contribute, star :star: the repository and create a fork, make changes, and create a pull request. <br>
<!-- > Note: Contributing to the research paper file will be highly appreciated but cannot get you considered as a co-author. <br> -->


## :page_facing_up: Research Paper
A pre-print of the research paper is available on [arXiv:2406.19271](https://arxiv.org/abs/2406.19271) <br>


## :bookmark_tabs: Citation
To use my paper for reference, please cite it as below:
```bibtex
@misc{vadlapati2024autopuredataautomatedfilteringweb,
	title={{AutoPureData: Automated Filtering of Web Data for LLM Fine-tuning}},
	author={Praneeth Vadlapati},
	year={2024},
	eprint={2406.19271},
	archivePrefix={arXiv},
	primaryClass={cs.CL},
	url={https://arxiv.org/abs/2406.19271}, 
}
```


## :identification_card: License
Copyright (c) 2024 Praneeth Vadlapati <br>
Please refer to the [LICENSE](./LICENSE.md) file for more information.


## :warning: Disclaimer
The code is not intended for use in production environments.
This code is for educational and research purposes only.

No author is responsible for any misuse or damage caused by this code.
Use it at your own risk. The code is provided as is without any guarantees or warranty.


## :globe_with_meridians: Acknowledgement  <!-- (works referred/cited) -->
- Dataset: HuggingFace FineWeb https://huggingface.co/datasets/HuggingFaceFW/fineweb
- Unsafe text detections: Meta Llama Guard 2 https://github.com/meta-llama/PurpleLlama/blob/main/Llama-Guard2/MODEL_CARD.md
- Other detections: Meta Llama 3 https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md
<!-- - Image credits: OpenAI DALL-E 3 https://openai.com/index/dall-e-3/ -->


## :email: Contact
For personal queries, please find my contact details here: [linktr.ee/prane.eth](https://linktr.ee/prane.eth)

<!-- star chart
https://starchart.cc/pro-GenAI/AutoPureData.svg -->
