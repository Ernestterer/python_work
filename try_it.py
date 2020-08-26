message = "ernest terer"
print(message.title())

first_name = "terer"
last_name = "ernest"
full_name = f"{first_name} {last_name}"#f stands for format. A new feature
print(full_name)
message = f"Hello, {full_name.title()}"
print(message)
print("Languages:\n\tC\n\tJavascript\n\tJava\n\t")

favourite_language = " Python  "
favourite_language = favourite_language.rstrip()#eliminate whitespaces on the right
print(favourite_language)
favourite_language = favourite_language.lstrip()#eliminate whitespaces on the left
print(favourite_language)
favourite_language = " Java "
favourite_language = favourite_language.strip()#eliminate whitespaces on both sides
print(favourite_language)
