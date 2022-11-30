def isValid(s: str) -> bool:
    openings = ['(', '{', '[']
    closings = [')', '}', ']']
    unclosed = []
    is_valid = True
    
    for i in range(len(s)):
        if s[i] in closings: # when you reach a closing bracket..
            closing_index = closings.index(s[i]) # ..check what type it is..
            if openings[closing_index] not in unclosed: # ..check if it has an open bracket from before..
                is_valid = False # .. if it doesn't, we've failed!
                break
            else: # but if it does have matching backet somewhere..
                # .. then check it is the most recent unclosed bracket..
                if unclosed[-1] == openings[closing_index]:
                    # ..then no longer track the opening bracket
                    unclosed.reverse()
                    unclosed.remove(openings[closing_index])
                    unclosed.reverse()
                else:
                    # otherwise, mismatch has occured 
                    is_invalid = False
                    break
        else: # when you reach an opening bracket..
            unclosed.append(s[i]) # ..keep track of it..
    
    # check if any unclosed brackets remain     
    is_valid = False if unclosed != [] else is_valid
    
    return is_valid


def test_isValid():
    # 1 - simple working case
    # 2 - simple unclosed case
    # 3 - simple unopened case
    # 3 - simple mismatch
    # 4 - correct nesting
    # 5 - incorrect nesting due to unclosed bracket
    # 6 - incorrect nesting due to wrong ordering
    # 7 - incorrect nesting due to mismatching
    # 8 - simple adjacent pairs
    overall_success = True
    test_inputs = ["()", "(", "]", "(]", "([])", "[{]", "([)]", "[{)]", "{}[]()"]
    test_output = [True, False, False, False, True, False, False, False, True]
    test_cases = dict(zip(test_inputs, test_output))
    
    for i in range(len(test_inputs)):
        true_output = isValid(test_inputs[i])
        is_success = (true_output == test_output[i])
        is_success_text = "PASS" if is_success else "FAIL"
        overall_success = False if is_success == False else overall_success 
        
        print(f"{i} : input='{test_inputs[i]}'")
        print(f"expected_output=\t{test_output[i]}")
        print(f"true_output=\t\t{true_output}")
        print()
        print(f"\t{is_success_text}")
        print()

    overall_success_text = "ALL TESTS PASSED" if overall_success else "TEST(S) FAILED"
    print(overall_success_text)

    
test_isValid()
