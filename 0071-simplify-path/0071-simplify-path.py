class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for dir_name in path.split('/'):
            if dir_name == '..':
                if stack:
                    stack.pop()
            elif dir_name and dir_name != '.':
                stack.append(dir_name)

        return '/' + '/'.join(stack)
