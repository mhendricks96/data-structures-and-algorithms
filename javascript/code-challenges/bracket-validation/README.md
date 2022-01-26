# Muilti-Bracket Validation

## Challenge

- write a function called validate brackets

## validateBrackets()

- Arguments: string

- Return: boolean representing wheter or tho the brackets in the string are balanced.

## Examples

- {}:TRUE
- {}(){}:TRUE
- ()[[Extra Characters]]:TRUE
- (){}[[]]:TRUE
- {}{Code}[Fellows](()):TRUE
- [({}]:FALSE
- (](:FALSE
- {(}):FALSE

## Approach & Efficiency

iterated through input and pushed opening brackets to stack. then check for a closing bracket to match every opening bracket
