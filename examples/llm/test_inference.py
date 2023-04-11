from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import AutoConfig

config = AutoConfig.from_pretrained('EleutherAI/gpt-neo-125m')

CHECKPOINT_DIR = './run125/hf_export'

model = AutoModelForCausalLM.from_pretrained(CHECKPOINT_DIR, config=config)

import code
code.interact(local=locals())
