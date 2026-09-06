FROM public.ecr.aws/lambda/python:3.8

COPY quesans/app.py ./
COPY requirements.txt ./

RUN python3.8 -m pip install -r requirements.txt

RUN python3.8 -c "from transformers import AutoTokenizer, AutoModelForQuestionAnswering; model_name='deepset/minilm-uncased-squad2'; AutoTokenizer.from_pretrained(model_name).save_pretrained('/opt/ml/model'); AutoModelForQuestionAnswering.from_pretrained(model_name).save_pretrained('/opt/ml/model')"

CMD ["app.handle_request"]