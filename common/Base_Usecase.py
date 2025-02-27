class Base_Usecase:
    def __init__(self, *args, **kwargs):
        pass
    
    def pre_processing(self, *args, **kwargs):
        raise NotImplementedError("pre_processing method is not implemented")

    def post_processing(self, result, *args, **kwargs):
        pass
    
    def run(self, process_data, *args, **kwargs):
        raise NotImplementedError("run method is not implemented")
    
    def execute(self, *args, **kwargs):
        processed_data = self.pre_processing(*args, **kwargs)
        result = self.run(processed_data, *args, **kwargs)
        self.post_processing(result, *args, **kwargs)
        return result