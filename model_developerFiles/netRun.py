from network_generation import Settings, Scenario
from optimization_model import optimization_model

settings = Settings(50,8,2,100)

scenario = Scenario(settings)
scenario.populate_scenario()

opt_model = optimization_model(scenario)
opt_model.create_model_variables()
opt_model.add_model_constraints()
opt_model.set_model_objective()
opt_model.write_model()
