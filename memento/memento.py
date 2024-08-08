class GameMemento:
    # inicia o memento com os valores do jogo
    def __init__(self, player_name, level, score):
        self.player_name = player_name
        self.level = level
        self.score = score

    # retorna os valores do jogo
    def get_player_name(self):
        return self.player_name

    def get_level(self):
        return self.level

    def get_score(self):
        return self.score


class Game:
    # inicia o jogo com valores padrão
    def __init__(self):
        self.player_name = ""
        self.level = 0
        self.score = 0

    # define o estado do jogo
    def set_state(self, player_name, level, score):
        self.player_name = player_name
        self.level = level
        self.score = score

    # salva o estado do jogo
    def save(self):
        return GameMemento(self.player_name, self.level, self.score)

    # carrega o estado do jogo
    def load(self, memento):
        self.player_name = memento.get_player_name()
        self.level = memento.get_level()
        self.score = memento.get_score()

    # retorna o estado do jogo
    def __str__(self):
        return f"Player: {self.player_name}, Level: {self.level}, Score: {self.score}"


class GameCaretaker:
    #inicia o caretaker com uma lista vazia de mementos e o índice atual como -1
    def __init__(self):
        self.mementos = []
        self.current_index = -1

    # salva o estado do jogo em mementos
    def save(self, game):
        # Remove any redo history
        self.mementos = self.mementos[:self.current_index + 1]
        self.mementos.append(game.save())
        self.current_index += 1

    # carrega os estados do jogo se existirem
    def load(self, game):
        if self.current_index < 0:
            print("No save states to load.")
            return
        game.load(self.mementos[self.current_index])

    # volta um estado do jogo
    def undo(self, game):
        if self.current_index <= 0:
            print("No previous states to undo.")
            return
        self.current_index -= 1
        game.load(self.mementos[self.current_index])

    # refaz um estado do jogo desfeito anteriormente
    def redo(self, game):
        if self.current_index >= len(self.mementos) - 1:
            print("No future states to redo.")
            return
        self.current_index += 1
        game.load(self.mementos[self.current_index])


# Exemplo de uso
if __name__ == "__main__":
    game = Game()
    caretaker = GameCaretaker()

    game.set_state("Player1", 1, 100)
    print(game)
    caretaker.save(game)

    game.set_state("Player1", 2, 200)
    print(game)
    caretaker.save(game)

    game.set_state("Player1", 3, 300)
    print(game)
    caretaker.save(game)

    caretaker.undo(game)
    print("After undo:", game)

    caretaker.undo(game)
    print("After second undo:", game)

    caretaker.redo(game)
    print("After redo:", game)
