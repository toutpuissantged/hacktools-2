
class Helpers():

    def __init__():
        pass

    @staticmethod 
    def time_builder(timer):
        timer=int(timer)
        time_schema={
			'heures':0,
			'minutes':0,
			'seconde':0,
		}
        minute=timer//60
        time_schema['seconde']=timer
        if (minute<1):
            return time_schema
        seconde=timer%60
        minute=timer//60
        time_schema['seconde']=seconde
        time_schema['minutes']=minute
        if (minute//60<1):
            return time_schema

        heures=minute//60
        minute=minute%60
        time_schema['heures']=heures
        time_schema['minutes']=minute

        return time_schema