a = open("status.html", "r", encoding="utf-8").read()
a = a.replace("To became główna teza projektu", "To jest główna teza projektu")
open("status.html", "w", encoding="utf-8").write(a)
print("fixed:", "became" not in a)