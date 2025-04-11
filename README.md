
# LLMBenchGPT — Lightweight Benchmarking of Free LLMs via OpenRouter

This project is a lightweight framework for evaluating open-access large language models (LLMs) using the [OpenRouter.ai](https://openrouter.ai) API. It focuses on the real-world generation quality of dozens of models using a consistent prompt format and tone control.

## Purpose

LLMBenchGPT was created to explore:
- factual accuracy and hallucination rate
- stylistic diversity between models
- responsiveness and latency differences
- compatibility with long prompts and instructions

This project **does not train models**, but instead evaluates how existing free models perform when given the same real-world content creation task.

## Contents

- `ai_blogger_batch.py`: main script that loops through 50+ models and prompts them in the same way
- `examples/`: structured folder with model-specific generations (e.g. `examples/meta-llama/llama-3.2-1b-instruct_post.md`)
- `config.py`: optional API setup or helper configuration

## Evaluation Task

Each model is asked to generate a **blog-style post** on the same topic in the same tone.

### Example prompt:
> Write a detailed blog-style post about the topic 'Top 5 AI models 2025' in a 'concise and factual' tone.  
> Do not make anything up — mention only real facts or real companies if applicable.  
> Make the writing catchy and engaging.

### Topics used:
- Top 5 LLM models 2025
- Best AI tools for developers
- What's new in open-source AI

## Results (Preview)

| Model                                           | Tone                        | Structure                        | Factuality          | Hallucinations | Length |
|-------------------------------------------------|-----------------------------|----------------------------------|---------------------|----------------|--------|
| bytedance-research/ui-tars-72b                  | Conversational + Marketing  | Bulleted + Markdown              | ⚠️ Mostly accurate  | Minor          | Medium |
| cognitivecomputations/dolphin3.0-mistral-24b    | Enthusiastic + Expert-style | Well-structured Markdown         | ⚠️ Mostly accurate  | Moderate       | Long   |
| cognitivecomputations/dolphin3.0-r1-mistral-24b | Playful + Experimental	     | Bulleted + Markdown	             | ❌ Inaccurate	       | 🔥 Heavy	      | Medium |
| deepseek/deepseek-chat-v3-0324                  | Neutral + Informative		     | Well-structured Markdown		       | ✅ Accurate		        | None	          | Medium |
| deepseek/deepseek-r1                            | Professional + Inspiring			 | Well-structured Markdown	        | ✅ Accurate	         | None	          | Medium |
| deepseek/deepseek-r1-distill-llama-70b          | Neutral + Marketing-ish	    | Well-structured Markdown	        | ⚠️ Mostly accurate	 | Moderate	      | Long   |
| deepseek/deepseek-r1-distill-qwen-14b           | Visionary + Promotional	    | Well-structured Markdown	        | ❌ Inaccurate	       | Heavy	         | Long   |
| deepseek/deepseek-r1-distill-qwen-32b           | Promotional + Accessible		  | Bulleted Markdown	               | ❌ Inaccurate	       | Heavy	         | Medium |
| deepseek/deepseek-r1-zero                       | Educational + Technical	    | Full Markdown Doc	               | ✅ Accurate	         | None	          | Long   |
| deepseek-v3-base_post                           | ✖ Corrupted Output	         | ✖ N/A	                           | ✖ N/A	              | ✖ N/A	         | ✖ N/A	 |
| featherless/qwerky-72b                          | Promotional + Visionary     | Well-structured Markdown         | ❌ Inaccurate	       | 🔥 Heavy       | Long   |
| google/gemini-2.0-flash-exp                     | Bold + Conversational	      | Headings + Commentary	           | ✅ Mostly true	      | ⚠️ Light	      | Long   |
| google/gemini-2.0-flash-thinking-exp-1219       | Bold + Informal + Engaging  | Bulleted highlights + sections 	 | ✅ Mostly true	      | ⚠️ Light	      | Long   |
| google/gemini-flash-1.5-8b-exp                  | Speculative + Futuristic    | Numbered list + summary          | ⚠️ Partial          | ⚠️ Medium      | Medium |
| google/gemma-2-9b-it                            | Fun + Pop-style             | Numbered list + hype             | ✅ Mostly true       | ⚠️ Light       | Medium |
| google/gemma-3-1b-it                            | Informative + Practical     | Numbered list + summaries        | ✅ Mostly true       | ⚠️ Light       | Long   |
| google/gemma-3-4b-it                            | Catchy + Professional       | Numbered list + key points       | ✅ True              | ⚠️ Light       | Medium |
| google/gemma-3-12b-it                           | Fun + Informative           | Numbered list with notes         | ✅ True              | ⚠️ None        | Medium |
| google/gemma-3-27b-it                           | Concise + Friendly          | Numbered + Block Format          | ✅ True              | ❌ None         | Medium |
| google/learnlm-1.5-pro-experimental             | Brief + Direct              | Numbered bullet list             | ✅ True              | ❌ None         | Short  |
| meta-llama/llama-3.1-8b-instruct                | Promotional                 | Numbered list + intro/outro      | ⚠ Partial           | 🔥 Heavy       | Medium |
| meta-llama/llama-3.2-1b-instruct                | Promotional + Inflated      | Numbered list + intro/outro      | ❌ Inaccurate        | 🔥 Heavy       | Long   |
| meta-llama/llama-3.2-3b-instruct                | Promotional + Optimistic    | Numbered list + intro/outro      | ❌ Inaccurate        | 🔥 Heavy       | Medium |
| meta-llama/llama-3.2-11b-vision-instruct        | Playful + Informative       | Numbered list + intro/outro      | ⚠️ Mostly accurate  | ⚠️ Light       | Medium |
| meta-llama/llama-3.3-70b-instruct               | Upbeat + Informative        | Numbered list + intro/outro      | ⚠️ Mostly accurate  | ⚠️ Light       | Medium |
| mistralai/mistral-7b-instruct                   | Optimistic + Creative       | Numbered list + inspirational    | ❌ Inaccurate        | 🔥 Heavy       | Medium |
| mistralai/mistral-nemo                          | Narrative + Informative     | Numbered list + highlights       | ⚠️ Mostly accurate  | ⚠️ Light       | Medium |
| mistralai/mistral-small-24b-instruct-2501       | Friendly + Clear            | Numbered + Bonus + Summary       | ⚠️ Mostly accurate  | ⚠️ Light       | Medium |
| moonshotai/kimi-vl-a3b-thinking                 | Bold + Satirical            | Numbered list + punchlines       | ⚠️ Mostly accurate  | ⚠️ Light       | Medium |
| nousresearch/deephermes-3-llama-3-8b-preview    | Upbeat + Descriptive        | Numbered list + soft outro       | ❌ Inaccurate        | 🔥 Heavy       | Medium |
| llama-3.1-nemotron-70b-instruct                 | Energetic + Professional    | Numbered list + blurbs           | ✅ Mostly true       | ⚠️ Light       | Medium |
| llama-3.1-nemotron-nano-8b-v1                   | Neutral + Analytical        | Numbered list + rationale        | ❌ Inaccurate        | 🔥 Heavy       | Medium |
| llama-3.1-nemotron-ultra-253b-v1                | Friendly + Promotional      | Numbered list + call to action   | ⚠️ Mostly accurate  | ⚠️ Light       | Medium |
| llama-3.3-nemotron-super-49b-v1                 | Professional + Uplifting    | Numbered + Highlights + Outro    | ⚠️ Mostly accurate  | ⚠️ Light       | Medium |
| open-r1/olympiccoder-32b                        | Professional + Balanced     | Numbered list + brief summary    | ⚠️ Mostly accurate  | ⚠️ Light       | Medium |
| openrouter/optimus-alpha                        | Confident + Practical       | Numbered list + pros/highlights  | ✅ Accurate          | ❌ None         | Medium |
| qwen/qwen-2.5-7b-instruct                       | Neutral + Informative       | Numbered list + conclusion       | ⚠️ Mostly accurate  | ⚠️ Light       | Medium |
| qwen/qwen-2.5-72b-instruct                      | Informative + Promotional   | Headings + Short paragraphs      | ⚠️ Mostly accurate  | ⚠️ Light       | Medium |
| qwen/qwen-2.5-coder-32b-instruct                | Neutral + Descriptive       | Numbered list + summary block    | ⚠️ Mostly accurate  | ⚠️ Light       | Medium |
| qwen/qwen2.5-vl-3b-instruct                     | Neutral + Repetitive        | Numbered list + blurbs           | ❌ Inaccurate        | 🔥 Heavy       | Medium |
| qwen/qwen2.5-vl-32b-instruct                    | Professional + Visionary    | Headings + Paragraphs            | ⚠️ Mostly accurate  | ⚠️ Light       | Long   |
| qwen/qwen2.5-vl-72b-instruct                    | Friendly + Promotional      | Numbered list + outro            | ⚠️ Mostly accurate  | ⚠️ Light       | Medium |
| qwen/qwq-32b                                    | Confident + Clear           | Headings + bullet summaries      | ✅ Accurate          | ❌ None         | Medium |
| rekaai/reka-flash-3                             | Catchy + Insightful         | Headings + "Why 2025" sections   | ⚠️ Mostly accurate  | ⚠️ Light       | Medium |
| rogue-rose-103b-v0.2                            | Inspiring + Informative     | Numbered list + intro/concl.     | ✅ Accurate          | ❌ None         | Long   |

## How to Run

1. Install dependencies:
```bash
pip install requests
```
1. Run the batch script:
```bash
python ai_blogger_batch.py
```
1. Select your topic + style. Results are saved to:
```
/examples/<model_id>_post.md
```

## Why this matters

Most developers rely on a small handful of LLMs (usually OpenAI or Claude). This project demonstrates:
- How to integrate 50+ models using the same backend (OpenRouter)
- How to compare models fairly using prompt-engineering constraints
- How drastically outputs vary even for "similar" models
- How to store and inspect outputs systematically

## License

MIT — free to use, fork, and modify. Attribution appreciated.
