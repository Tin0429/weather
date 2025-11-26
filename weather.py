import requests

class WeatherReActAgent:
    def __init__(self, api_key):
        self.api_key = api_key

    def think(self, query):
        # Simple reasoning
        if "天氣" in query or "weather" in query:
            return "查詢天氣"
        return "無法處理的任務"

    def act(self, action, location="Taoyuan"):
        if action == "查詢天氣":
            url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={self.api_key}&lang=zh_tw&units=metric"
            response = requests.get(url).json()
            return response
        return None

    def answer(self, query, location="Taoyuan"):
        action = self.think(query)
        data = self.act(action, location)

        if not data or "weather" not in data:
            return "抱歉，我無法取得天氣資訊。"

        desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]

        return f"現在{location}的天氣是 {desc}，溫度約 {temp}°C。"


agent = WeatherReActAgent(api_key="8f2d23f2f89c1b9602408a18bab904e0")
print(agent.answer("幫我查天氣", location="Taoyuan"))