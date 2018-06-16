
# Auxílios

1 - Localizar caminho absoluto de um arquivo python executando

```python
import os

caminho_absoluto = os.path.dirname(os.path.realpath(__file__))
```

> O código acima possibilita encontrar o caminho absoluto de um arquivo python