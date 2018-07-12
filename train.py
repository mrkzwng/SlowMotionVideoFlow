import Train

trainer = Train(
    'tmp/',
    'models/iter_0/',
    '../data/check/',
    'avi',
    128,
    128
)
trainer.train()