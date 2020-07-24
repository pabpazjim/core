from famapy.core.discover import DiscoverMetamodels


dm = DiscoverMetamodels()

""" Esto para futuro
1. ¿que hacer?
[tranform, operate]

- tranform: t2m, m2t, m2m
    src, dst, filename, variability_model

- operate: sobre un model, pedirá un variability_model y una operación
"""

# Example m2t
#TODO debe recibir un VM del cual sacamos el metamodelo
dm.use_transformation_m2t(orig: VariabilityModel, dst='/tmp/output.json')

# Example t2m
#TODO debe devolver un modelo
dm.use_transformation_t2m(dst='fm', orig='/tmp/in.xml')  # vamos a usar la extensión

# Example m2m
dm.use_transformation_m2m(orig=VariabilityModel, dst='fm')  # devolver instancia del tipo fm


dm.use_operation(orig: VariabilityModel, op: Operation)
