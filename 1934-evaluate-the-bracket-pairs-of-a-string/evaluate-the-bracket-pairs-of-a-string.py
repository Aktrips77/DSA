class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Step 1: Create a lookup dictionary from the knowledge array
        kv_map = {key: value for key, value in knowledge}
        
        result = []
        current_key = []
        is_inside_bracket = False
        
        # Step 2: Parse the string in a single pass
        for char in s:
            if char == '(':
                is_inside_bracket = True
            elif char == ')':
                is_inside_bracket = False
                key_str = "".join(current_key)
                
                # O(1) Lookup: Append value if key exists, else '?'
                if key_str in kv_map:
                    result.append(kv_map[key_str])
                else:
                    result.append('?')
                    
                current_key.clear() # Reset for the next bracket pair
            else:
                if is_inside_bracket:
                    current_key.append(char)
                else:
                    result.append(char)
                    
        return "".join(result)
