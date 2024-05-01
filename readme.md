# Projeto de Gerenciamento de Dependências
## Detalhamento dos Requisitos

### Funcionalidades
*Adicionar Dependência*: O sistema deve permitir que o usuário adicione uma nova dependência ao projeto, especificando o nome da dependência e sua versão.

Remover Dependência: O sistema deve permitir que o usuário remova uma dependência existente, selecionando-a a partir de uma lista de dependências atuais.

Listar Dependências: O sistema deve exibir todas as dependências associadas ao projeto, incluindo nome e versão.

Atualizar Dependência: O sistema deve permitir que o usuário atualize a versão de uma dependência existente.

### Interface do Usuário
Interface baseada em texto com um menu de opções, permitindo ao usuário escolher entre adicionar, remover, listar ou atualizar dependências.
### Persistência de Dados
Os dados das dependências devem ser armazenados em um arquivo CSV, permitindo fácil manipulação e recuperação.
### Restrições e Regras de Negócio
As entradas de dependências devem ser validadas para garantir que o nome e a versão não estejam vazios.
Não deve ser possível adicionar uma dependência com o mesmo nome, a menos que seja para atualizar sua versão. 

## Testes com Plano, Roteiro e Evidências

### Plano de Testes
Objetivo: Verificar se todas as funcionalidades do sistema de gestão de dependências estão funcionando como esperado.
Método: Testes manuais e automatizados.
### Roteiro de Testes
#### Testar Adição de Dependência:

Cenário: Adicionar uma nova dependência.

Passos: Acessar a opção de adicionar, inserir o nome e a versão, verificar se a dependência foi adicionada corretamente.

Resultado Esperado: A dependência é adicionada ao arquivo CSV.

#### Testar Remoção de Dependência:

Cenário: Remover uma dependência existente.

Passos: Acessar a opção de remover, inserir o nome da dependência, verificar se foi removida.

Resultado Esperado: A dependência é removida do arquivo CSV.

#### Testar Listagem de Dependências:

Cenário: Listar todas as dependências.

Passos: Acessar a opção de listar, verificar a listagem.

Resultado Esperado: Todas as dependências são listadas com seus respectivos nomes e versões.

#### Testar Atualização de Dependência:
Cenário: Atualizar a versão de uma dependência existente.

Passos: Acessar a opção de atualizar, inserir o nome da dependência e a nova versão, verificar a atualização.

Resultado Esperado: A dependência tem sua versão atualizada no arquivo CSV.

### Evidências de Teste
Os testes tiveram resultado...
