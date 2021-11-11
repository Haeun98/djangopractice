from django.http import HttpResponse

def index(request ,name, age):
    message = "\"hello, " + age + " years old " + name +"!\""
    output = "{\n" + "\t\"name\": \"" + name + "\",\n\t\"age\": " + age + ",\n\t\"message\": " + message + "\n}"
    return HttpResponse(output, content_type="text/plain")
