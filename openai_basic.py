#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:05:04 2023

@author: John Ciubuc
"""
import openai
class openai_basic:
    _model = "gpt-3.5-turbo"
    def __init__(self):
        openai.api_key_path = '/home/inathero/openai_temp_key'
        self.reset_messages()
    def reset_messages(self):
        self._messages = [
            {"role": "system", "content": "you are a highly advanced AI trained in internal medicine and medical education. Your role is an educator that asks students critical thinking questions as they develop their assessment and plan. Examples of this are 'what do you think is happening' and 'what can make this patient sicker'"},
            ]
    def reset_messages_set_patient(self, patient_text):
        self.reset_messages()
        self._messages.append({"role": "system", "content": patient_text})
    def append_student_response(self, student_response):
        self._messages.append({"role": "user", "content": student_response})
    def append_ai_question(self, educator_response):
        self._messages.append({"role": "assistant", "content": educator_response})
    def query(self):
        response= openai.ChatCompletion.create(
          model=self._model,
          messages=self._messages
        )
        response_message = response.choices[0]["message"]["content"]
        self.append_ai_question(response_message)
        return response_message
