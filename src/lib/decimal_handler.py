class DecimalHandler:
    def is_float(self, param: str) -> bool:
        if not param.isdecimal():
            try:
                float(param)
                return True
            except ValueError:
                return False
        else:
            return False
