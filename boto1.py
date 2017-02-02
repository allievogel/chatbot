    from bottle import route, run, template, static_file, request, response
    import json
    import random
    from random import randint
    import datetime


    @route('/', method='GET')
    def index():
        return template("chatbot.html")


    def in_news(command):
        if "what" not in command:
            return "Please ask a valid question starting by what..."
        url = "https://newsapi.org/v1/articles?source=techcrunch&apiKey={a770dce3d8b8409a95b948bc021d7280}"
        response = requests.get(url)
        data = response.json()
        print(data)
        return "{} is the latest in the news".format()


    def curse_words(command):
        if curse_words in command:
            return "Potty mouth! Don't you curse at me..."


    def awesome(command):
        if awesome in command:
            return "Did you know you are my favorite person, ever!"


    def your_name(command):
        if "name is" in command:
            info['your_name'] = command.split("name is ")[1].split(" ")[0]
        else:
            info['your_name'] = command
        return "Nice to meet you, {}".format(info['your_name'])


    any_terms = [
        {
            "words": [line.strip() for line in open("list_bad_words.txt", 'r')],
            "handler": curse_words,
            "animation": 'crying'
        },
        {
            "words": ['Nathalie', 'Arie' 'Gideon', 'Allie', 'Olivia', 'Gilad'],
            "handler": awesome,
            "animation": 'dancing'
        },
    ]
    all_terms = [
        {
            "words": ["what", "your", "name"],
            "handler": your_name,
            "animation": "giggling"
        },
    ]


    @route("/chat", method='POST')
    def chat():
        user_message = request.POST.get('msg')

        return analyze_command()


    # json.dumps({"animation": "giggling", "msg": user_message})

    # solution function
    def analyze_command():
        # for term in any_terms:
        #     if any(x in command for x in term["words"]):
        #         return term["handler"](command), term["animation"]
        # for term in all_terms:
        #     if all(x in command for x in term["words"]):
        #         return term["handler"](command), term["animation"]
        # if not info["first_message"]:
        #     info["first_message"] = True
        return json.dumps({"animation": "confused", "msg": "Sorry, I'\m not sure what you mean by that"})


    # predefined
    @route("/test", method='POST')
    def chat():
        user_message = request.POST.get('msg')
        return json.dumps({"animation": "giggling", "msg": user_message})


    @route('/js/<filename:re:.*\.js>', method='GET')
    def javascripts(filename):
        return static_file(filename, root='js')


    @route('/css/<filename:re:.*\.css>', method='GET')
    def stylesheets(filename):
        return static_file(filename, root='css')


    @route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
    def images(filename):
        return static_file(filename, root='images')


    def main():
        run(host='localhost', port=7006)


    if __name__ == '__main__':
        main()