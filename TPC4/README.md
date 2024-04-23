# TPC2 : Construir um analisador léxico

## Aluno

**Nome:** Francisco Lameirão

**Número:** a97504

## TPC

O objetivo deste TPC é construir um analisador léxico para analisar expressões SELECT como usado em SQL.

Por exemplo, para a expressão:

```sql
SELECT name, age FROM people WHERE age > 18;
```

O analisador léxico deve ser capaz de identificar os tokens `SELECT`, `name`, `,`, `age`, `FROM`, `people`, `WHERE`, `age`, `>`, `18`, `;`.
