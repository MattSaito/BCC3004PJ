Este Repositório é dedicado a disciplina de engenharia de software BCC3004, para o conteúdo de padrão de projeto:

# Padrões de Projeto 

Padrões de Projeto são soluções para problemas comuns encontrados durante projetos de software,representando melhores práticas 
que desenvolvedores podem seguir para resolver e evitar estes problemas de forma eficiente.

Os principais grupos de padrões de projeto:

Padrões Criacionais: focados em otimizar o processo de criação de objetos, ajudam a controlar como os objetos são instanciados,
são exemplos: Singleton, Prototype, Builder , etc...

Padrões Estruturais: focados em organizar e relacionar objetos de forma que se torne mais facil a construção e manutenção de sistemas complexos,
são exemplos: Bridge, Decorator, Proxy , etc...

Padrões Comportamentais: focados em comunicação e interação entre objetos distribuindo responsabilidades e melhorando flexibilidade dos sistemas,
são exemplos: Chain of responsability, Memento, Command, etc...


## Prototype(Criacional)

O Prototype permite copiar objetos existentes sem causar uma dependência das classes, o que é util quando o processo de criação ou inicialização
de objetos é demorada ou complexa e também quando um objeto é privado ou possui campos privados.

Sendo assim o padrão declara uma classe ou interface comum para permitir a clonagem como pode ser visto no codigo implementado ["prototype.py"](prototype/prototype.py),
que possui uma função de clonagem para que seja facilitado essa cópia de um objeto.

Exemplo:
 ```python 
    def clone(self):
        return copy.deepcopy(self)
```
esta função de clonagem faz parte da propria classe Animal e se for necessário a clonagem de outro animal com as mesmas características podemos utiliza-la: 
 ```python
    another_dog = dog_prototype.clone()
    another_cat = cat_prototype.clone()
```

## Proxy(Estrutural)

O proxy serve como um gerenciador de acesso a um objeto, ao invés de acessar um objeto diretamente é criado um proxy para mediar esta interação, isto é util em ocasiões como proteção de acesso por exemplo.
Sendo assim temos: 

Subject (Sujeito): Define a interface comum entre o Proxy e o objeto real, garantindo que ambos possam ser usados de forma intercambiável pelo cliente.

RealSubject (Objeto Real): É a classe que implementa a funcionalidade real. Este é o objeto que realiza as operações concretas e que o Proxy controla ou substitui.

Proxy: Implementa a interface do Subject e mantém uma referência ao Objeto Real. O Proxy gerencia o acesso ao Objeto Real e pode implementar funcionalidades adicionais, como controle de acesso, criação adiada, ou cache.

Exemplo utilizando ["proxy.py"](proxy/proxy.py)

Definição de Interface Comum: O FirewallProxy atua como uma interface intermediária entre o cliente e o servidor real. Embora não haja uma interface explícita no código, o FirewallProxy fornece a mesma interface que o servidor real para os clientes (recebe solicitações e envia respostas).

Controle de Acesso: O FirewallProxy implementa um controle de acesso ao verificar se o domínio solicitado é permitido (self.allowed_domains). Isso é uma forma de controle de acesso, típico do Proxy Protection, que restringe quais domínios podem ser acessados.

Encaminhamento de Solicitações: O FirewallProxy lida com a solicitação recebida do cliente e, se o domínio estiver permitido, encaminha a solicitação para o servidor real (server_socket.connect((host, 80))). Após receber a resposta do servidor real, o Proxy a encaminha de volta para o cliente. Atuando como um intermediário entre o cliente e o objeto real.

Criação e Manuseio do Objeto Real: O FirewallProxy cria e gerencia uma conexão com o servidor real (server_socket), o que demonstra a responsabilidade de um Proxy de lidar com a criação e o gerenciamento do objeto real, neste caso, a comunicação com o servidor.


## Memento(Comportamental)

O memento permite que um estado anterior de um objeto seja salvo e restaurado de acordo com a necessidade para isto temos:

Memento: Representa o estado interno do objeto no momento em que o memento foi criado. Este objeto é normalmente implementado como uma classe com métodos para armazenar e recuperar o estado, sem expor a estrutura interna do objeto original.

Originador: É o objeto cujo estado precisa ser salvo e restaurado. Ele é responsável por criar um memento para armazenar seu estado atual e também pode usar um memento para restaurar seu estado para o ponto em que foi salvo.

Caretaker: É o responsável por gerenciar os mementos. Ele armazena e mantém os mementos criados pelo originador, mas não deve manipular nem examinar o conteúdo dos mementos. Seu papel é garantir que o memento correto seja recuperado quando necessário.

[Exemplo](memento/memento.py)

