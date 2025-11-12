It is a open source framework that help to build LLM application , Vo provide krta he modular component and end-to-end tool jo madad krte he complex AI application such as chatbot ,Q&A system , RAG(retrieval argument generations) ets. Langchain is a open-source framework  for developing application powered by large language model (LLM)
 
### GenAI 
Generation AI is a type of a that can create new content --such as that text can create image image , music or code -- by learning pattern 

![[GenAI  foundation model.canvas]]
#### Langchain ke type :
isme mainly 6 type me divide kya he or vo sare type niche given he :-
![[Langchain.canvas]]
## Models : 
The  models component in langchain is crucial part of the framwork , design to facilitate interaction with various Large language model and embedding model 
**In langchain "models" are the core interface through which you intreact with ai model
![[Models.canvas]]**
###### language models:
Are AI system designed to process , generate and understand natural language text 
- **LLm**s = It is General-perpose model that use to raw that generation ,{matlab ye sirf raw data he without tuning }
- **Chatmodel** = Lnaguage model that specialized for conversational Task
```
# step  for setup :
- create folder
- open in VS code 
- Create A new venv
   python -m venv venv
- Acticate venv
   venv\Scripts\Activate 
- create the requirement.txt use ye past kr do isme phele se hi importent library    he 
    # LangChain Core
	langchain
	langchain-core
	
	# OpenAI Integration
	langchain-openai
	openai
	
	# Anthropic Integration
	langchain-anthropic
	
	# Google Gemini (PaLM) Integration
	langchain-google-genai
	google-generativeai
	
	# Hugging Face Integration
	langchain-huggingface
	transformers
	huggingface-hub
	
	# Environment Variable Management
	python-dotenv
	
	# Machine Learning Utilities
	numpy
	scikit-learn
- install packege from requirement.txt
   PIP install -r requirement.txt

```

###### temperature :
It is a parameter that control the randomness of a language model inputs . It effects how the model is creative or not 
   **the response are** :
   - factual answers  ---- 0.0 - 0.3
   - Balance response --- 0.5 - 0.7
   - Creative writing --- 0.9 - 1.2
   - maximum randomness --- 1.5+

###### Open source model :
open source model are freely available AI model that can be downloaded modified , fine tuning and develop without roktok ke .
###### Hugging face model : The largest Open source model library
hamare pass do tarike he isse use krne ke liye 
- using HF inferences API
- Running locally 

###### Embedded model :
ye ek model he jo ko number (vector) me convert krta he taki machine ko samj aye isse me pure pdf me koi bhi topic find kr skte he a ya kisi book me koi sa page 

## prompt : 
prompt are the input instruction or queries given to a model that show possible output ,
**LLM < ---> input <--->prompt**   ,basically jo ham llm ko dete he or usse output mangte he uske liye ye use atte he prompt **and prompt ke mainly 2 type hote he** 

   - A **static prompt** is hardcoded — the same message goes every time. Great for basic use cases.
```
	from langchain.prompts import ChatPromptTemplate
	from langchain_core.messages import HumanMessage
	from langchain_openai import ChatOpenAI
	
	prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}.")
	formatted_prompt = prompt.format_messages(topic="engineers")
	
	model = ChatOpenAI(model="gpt-3.5-turbo")
	response = model.invoke(formatted_prompt)
	print(response.content)

```

   - **Dynamic prompts** adapt based on user input, context, or variables. Perfect for chatbots, apps, or workflows.
```
    from langchain.prompts import ChatPromptTemplate
	from langchain_core.messages import HumanMessage
	from langchain_openai import ChatOpenAI
	import streamlit as st
	from dotenv import load_dotenv
	
	load_dotenv()
	model = ChatOpenAI(model="gpt-3.5-turbo")
	
	st.title(" Dynamic Prompt Demo")
	topic = st.text_input("Enter a topic:")
	
	if st.button("Generate Joke") and topic:
	    prompt = ChatPromptTemplate.from_template("Tell me a hilarious joke about          {topic}.")
	    messages = prompt.format_messages(topic=topic)
	
	    response = model.invoke(messages)
	    st.write(response.content)

```

Q. Why  we use Prompt templates over  F string ?
 - default validation
 - reusable
 - Langchain Ecosystem
###### **Message :**
LangChain me `message` ka matlab hota hai — **AI aur user ke beech ke chat ke individual parts**. Har message ek specific type ka hota ha
![[Message type.canvas]]
###### **Message Placeholder :**
a message place holder in langchain is a special placeholder use inside a chatPromptTemplate to dynamically insert history or list of message  at runtime .
isse hum use karte he jab hame kisi particular person ki chat history mantain krni hoti he ny its id
###### **Structure Output :**
**Structure output** ka matlab hota hai jese me ChatGPT se bolu mujhe list do —  
**Do this in table form.** So yeh vo data ko well-mention form me mention karne ka hota hai.
 **Use Case:**
- Data Extraction
- API Building
- Agents
```
    Model.invoke (data format)
     /     |       \
   TypedDict  Pydantic   JSON-Schema
```

**TypedDict** :`TypedDict` is a way to define a dictionary in Python where you specify what key and value should exist.  It helps your dict follow a specific structure.

**Pydantic** = Pydantic is a data validation and parsing library for Python. It ensures that the data you work with is correct, structured, and type-safe.

###### **Output Parser :**
Output parser in **LangChain** helps convert raw LLM response format like **JSON**, **CSV**, and more.  
They ensure **consistency**, **validation**, and ease of use in applications.

**We can use this for:**

| Structured response by LLM | Unstructured response by LLM |
| -------------------------- | ---------------------------- |

- The **StrOutputParser** converts output in **string**
- The **JSONOutputParser** converts output in **JSON**.
- **StructuredOutputParser** is an output parser in LangChain that helps extract JSON data from LLM responses based on **predefined field schemas** (ye pehle se hi field define honi chahiye).
    - Isme ek kami ye hoti hai ki ye **data validation** nahi karta.
- **PydanticOutputParser** is a **structured output parser** in LangChain.
    - It uses the **Pydantic model** for **data schema validation**.

## chains :
A Chain is a sequence of calls where the output of one step becomes the input of the next.
ye ek flow mentain krte ke kese logically koi bhi message ya user input ke kaam hoga

![[chain.canvas]]
###### **type of chain :**
- **LLMChain** = Simplest chain – Prompt → LLM → Output
- **SimpleSequentialChain** =	Runs one chain after another (no logic between)
- **SequentialChain** =	Same as above but allows for memory passing between steps
- **ConversationChain** =	Maintains chat history (memory) — great for chatbots
- **RetrievalQAChain** =	Adds a retriever (like vector DB) to fetch context & answer
- **StuffDocumentsChain** = Stuff all docs into prompt & then run

###### **Runnable:**
A **Runnable** in LangChain is like a _Lego block for AI workflows_. It’s a **standard interface** that lets you **chain together any component** (LLMs, prompts, tools, retrievers, memory, etc.) in a _clean, reusable_ way.

## indexes :
It connect you application ot external knowledge base -- matlab required  data base jo LLM ko decision lene me help karte he such as PDFs, Website , Blogs
## Memory :
LLM ke pass koi building memory nhi hoti ager ham usse koi context pe baat kr rhe  he or uske baat ager contxt change krte he ho usse phle vala yaad ni rheta in simple iske  pas privious chat ki history nhi hoti vo hame build krni hoti he 
## Agents :
ye ek kind or chatbot hote but isme ek functionally jyada hoti he chat bot se ye realtime tool ta software ke sath kaaam kr skte he jese call , mail etc




