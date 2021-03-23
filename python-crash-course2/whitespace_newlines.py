# print('Python')
# print('\tPython')
# print('Languages:\nPython\nC\nJavaScript\n')
# print("Languages:\n\tPython\n\tC\n\tJavaScript")
# print()

favorite_language = ' python    '
print(favorite_language)
print(len(favorite_language))
print(favorite_language.rstrip()) ## Limpa todos os espaços à direita da string, mas apenas temporiariamente
print(len(favorite_language.rstrip()))
print()

language = 'javascript    '
print(len(language))
language = language.rstrip() ## Retirar espaços à direita permanentemente
print(len(language))
print()

whitespaces = '     whitespaces     '
print(len(whitespaces.strip()))  ## Retirar espaçoes de ambos lados