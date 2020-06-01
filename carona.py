import requests
import json
import pyttsx3


API_KEY="tjhzNQpJ3xfy"
PROJECT_TOKEN="tGEtaNCGHDTG"
RUN_TOKEN="tdyeaT2DVN4c"

class Data:
	def __init__(self, api_key, project_token):
		self.api_key = api_key
		self.project_token = project_token
		self.params = {
			"api_key": self.api_key
		}
		self.get_data()

	def get_data(self):
		response = requests.get(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/last_ready_run/data', params=self.params)
		self.data = json.loads(response.text)

	def get_total_case(self):
		data=self.data['total']
		for content in data:
			if(content['name']=="Coronavirus Cases:"):
				return content['value']
		return "0"

	def get_total_death(self):
		data=self.data['total']
		for content in data:
			if(content['name']=="Deaths:"):
				return content['value']
		return "0"

	def get_country(self):
		data=self.data['country']
		for content in data:
			print("\n")
			print("*\tCountry Name : ",content['name'])
			print("*\tTotal Cases : ",content['total_cases'])
			 		
			
			print("*\tTotal Recovered : ",content['total_recovered'])
			print("*****************************************")
			print("\n")
		return "0"

	def get_country_data(self,country):
		data=self.data['country']
		for content in data:
			if(content['name'].lower()==country.lower()):
				print("\n")
				print("*****************************************")
				print("*\tCountry Name : ",content['name'])
				print("*\tTotal Cases : ",content['total_cases'])
				print("*\tTotal Deaths : ",content['total_deaths'])
				print("*\tTotal Recovered : ",content['total_recovered'])
				print("*****************************************")
				print("\n")
		return "0"
		 

data=Data(API_KEY,PROJECT_TOKEN)
while 1 :
	print("==============================================================================")
	print("\t\t\t\tWelcome to CoronaVirus Update Portal")
	print("==============================================================================")
	print("\n")
	print("\t\tChoose 1. Global CaronaVirus Case : ")
	print("\t\tChoose 2. Global CaronaVirus Deaths : ")
	print("\t\tChoose 3. Total Coutrywise CaronaVirus Data : ")
	print("\t\tChoose 4. For Any Specific Country Update : ")
	print("\t\tChoose 5. Exit : ")
	print("\n")
	print("===============================================================================")
	x=int(input("Enter Your Choice : "))
	if(x==1):
		print("Total Global CaronaVirus Cases : ",data.get_total_case(),"\n")
	elif(x==2):
		print("Total Global CaronaVirus Deaths :", data.get_total_death(),"\n")
	elif(x==3):
		print("Country : \n",data.get_country())
	elif(x==4):
		y=input("Enter Country Name : ")
		print(data.get_country_data(y))
	elif(x==5):
		break;
	else:
		print("wrong Choice ! ")
