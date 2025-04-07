from crewai.flow.flow import Flow, listen, start
from litellm import completion

class ExampleFlow(Flow):

    model="gemini/gemini-1.5-flash"

    
    @start()
    def generate_city(self):
        random_cities = []
        for i in range(3):
            response = completion(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": f"Return the name of a random city in the world except for the cities that are already in {random_cities}. if there are no cities in the list, just return the name of any city. Do not return any other text.",
                    },
                ],
            )

            city = response["choices"][0]["message"]["content"]
            random_cities.append(city)


        self.state["random_cities"] = random_cities
        print(f"3 Random Cities:")
        for city in random_cities :
            print(f"{city}")
        return random_cities

    @listen(generate_city)
    def generate_fun_fact(self, random_cities):
        fun_facts = []
        for city in random_cities:
            response = completion(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": f"Tell me a fun fact about {city}",
                    },
                ],
            )

            fun_fact = response["choices"][0]["message"]["content"]
            fun_facts.append(fun_fact)

        self.state["fun_facts"] = fun_facts
        print("Fun Facts:")

        for i in range(len(random_cities)):
            print(f"City {i+1}: {random_cities[i]} - Fun fact: {fun_facts[i]}")

        return fun_facts

    @listen(generate_fun_fact)
    def rate_city(self, fun_facts):
        city_ratings = []
        cities =  self.state["random_cities"] 
        print("City Ratings:")
        for i in range(len(cities)):
            response = completion(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": f"rate the {cities[i]} based on it's fun fact {fun_facts[i]}",
                    },
                ],
            )

            city_rating = response["choices"][0]["message"]["content"]
            city_ratings.append(city_rating)
            print(f"{cities[i]}: {city_ratings[i]}")


        self.state["city_ratings"] = city_ratings
        return city_ratings


    @listen(rate_city)
    def best_city(self,city_ratings):
        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"Which city is the best based on the ratings {city_ratings}",
                },
            ],
        )

        best_city = response["choices"][0]["message"]["content"]
        print("The best city: ")
        print(f"{best_city}")
        return best_city

def kickoff():
    flow = ExampleFlow()
    flow.kickoff()


