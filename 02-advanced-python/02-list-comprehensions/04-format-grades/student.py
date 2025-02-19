def format_grades(grades):
    def average(ns):
        return round(sum(ns) / len(ns))
    
    return '\n'.join( f'{name}: {average(grade)}' for name, grade in grades.items() )