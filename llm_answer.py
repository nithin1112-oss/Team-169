from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def generate_answer(question, context):
    result = qa_pipeline({
        'context': context,
        'question': question
    })
    return result['answer']
