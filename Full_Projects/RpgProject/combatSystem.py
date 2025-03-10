""" FUNCTION battle(player, enemy):
    WHILE player.is_alive() AND enemy.is_alive():
        PRINT "Player Turn - Choose Action"
        DISPLAY options: "Attack" (more actions later)
        
        IF "Attack" selected:
            CALL player.attack(enemy)

        IF enemy.is_alive():
            PRINT "Enemy attacks!"
            CALL enemy.attack(player)
        
    IF player.is_alive():
        PRINT "You won!"
    ELSE:
        PRINT "You lost!" """
        
