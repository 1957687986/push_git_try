import torch

print("train:",len(train_db),"test:",len(test_db))

train_db, val_db = torch.utils.data.random_split(train_db, [50000,10000])

print("db1:",len(train_db),"db2",len(val_db))

train_loader = torch.utils.data.DataLoader(
    train_db,
    batch_size=batch_size,shuffle=True
)
val_loader = torch.utils.data.DataLoader(
    val_db,
    batch_size=batch_size,shuffle=True
)