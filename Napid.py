score = 0  # naprzyklad

#wynik napis
font = pygame.font.Font('freesansbold.ttf', 32) # czcionka (darmowa jedyna od pygame) i wielkość w pix
textX = 10 # Gdzie ma być (np. u gury w lewiej stronie)
textY = 10

def show_score(x, y):  # Pokazywanie wyniku
    scoreText = font.render('wynik: ' + str(score), True, (0, 0, 0)) #renderowanie textu - wynik: np.15 i kolor
    screen.blit(scoreText, (x, y))  #wyświetlanie
    global dirtyRects# żeby fajnie się odświerzało
    dirtyRects.append(r)

show_score(textX, textY)