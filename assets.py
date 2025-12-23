# assets.py
CATEGORIES = [
    {"name": 'Perros', "image": 'https://lh3.googleusercontent.com/aida-public/AB6AXuBxJJZQSRTQ0d3RKsd0GOtVnS2laFdNxXf9XMNVqwESzzv5kQHJ4FIAMm94jgbMECYVE0KC95XAsPxbd7Fg6y4TJkwqixQKRRS2SCWdT5Bd8EZbrGMfX8_csIhZQ2uBErN0k2drBCBhCSyfI7V78EQ6q_2vg94eFt95QP4FGgrPDnAZkKBT-XYRnxYXkDOBfjR52nT9wvepDdpoaLuaPGc18T3I988FjsB_fm1idg_rpi7_BFnQqEj7mtVp6fjDEPHMsZfOL2Zowms'},
    {"name": 'Gatos', "image": 'https://lh3.googleusercontent.com/aida-public/AB6AXuDLvRHsyjVQP1uhoCOkONZCFixnoFHiw5Z1xtRkqK4V4pblh4UkWmnuKV_2P3TR27duVlNHU6s36T32AcImaBNFrW7eznG5lfP0UnlX5TyS7u27uCWU81sTzkPnxh4WDgZ1QOk3qNwQFRYpKKXiIEJP2WIA6hZuiHDYi66VDrNsP2f0G-h5749WP_z-pKIZKSqJ2QSNMDWjRnyY5MuyRcFX75jmgdkE3Dh62ZNN0YCfgrCYige7tbZdWzwOG13ZXsJPW-mBmsaM-Gg'},
    {"name": 'Limpieza', "image": 'https://lh3.googleusercontent.com/aida-public/AB6AXuBsKUPgikB3fJs3ojUHfn_CM-8Dy6PtMWCV1M6dGElH5ReNOAbRGCTZK1U_zxNCOR9ol-qgfzVtVP_XnB5ygpins7xh17Jd5gEguXz4-WzTy3pvEi5Bo2JFvIBrOl8kq6nDn-5CmZ68LrLaDdhdXw7aiyLOAqF0yjIwoVWIttgbmCNaVWMHJwmeYgr6Vu4hpIuxDJGMag_TbD453HanYAP4kIW1qBgZL2wiEC_k97dey-SZmfRJRGOtSLo6HxAtA3QK9zSc-LlEb1I'},
    {"name": 'Accesorios', "image": 'https://lh3.googleusercontent.com/aida-public/AB6AXuDrzlDhbGO8MTcJcZxJANrICy-xhP89_rBDxjx0tK2Z8HsCGtZihpmd21FiDgnwMuZeYSsuiQTdjNVNCZ6x9MvoEUVHTxATxSyVEbrhIl3BJRJc-COSOAE2LPDKCvtjntIIzf5Uezv-85VQWu43eaVHB_Aco7_n_bt6pC9mYYSTzfaShdSLQFZObH-MMMo4XzKV9tScapf6SeJrD-9jW2lDRoF-truwTBfH9pkTkbmzLD0JCUqhkHbxrTz9iAC35Mnnr0QHJwpk1YA'},
]

PRODUCTS = [
    {
        "id": 1,
        "name": 'Ricocan Cordero y Cereales 15kg',
        "category": 'Perros - Alimento Seco',
        "price": 119.00,
        "originalPrice": 140.00,
        "image": 'https://lh3.googleusercontent.com/aida-public/AB6AXuB3Z1LMZsb74Tgm4Cdh1NMPZkSL8GB__pXbsiyqQiyL2faccfvknLupd0mIUrZUg21s-PggD_RMTBlxDgiiaiSilpfny7A0F9W31Cv2Em_QRo1wYXLs1RcxPnAMj4rJqn4YxlTUp3ac9Rqp-fRTxVYJI4jO__tswqLtZH-ucX4STrjSFuNuIZMutrtmJQAVPwMuOKrC7j6ng0L3vIc-tYRfzwfaLRnHRKhNPNhq48nkeD6ewUYIpuckVMjlRwX0CGiB8OcovDKBUA8',
        "badge": '-15%',
        "description": 'Saco 15kg'
    },
    {
        "id": 2,
        "name": 'Ricocat Atún y Sardinas 9kg',
        "category": 'Gatos - Alimento Seco',
        "price": 85.00,
        "originalPrice": 0,
        "image": 'https://lh3.googleusercontent.com/aida-public/AB6AXuBKCo8V8QDG2SAZBukKaZ8D8HDpP5iAdequtjJM52Cl7DdstyFKI-h5bT7ikgc6akCZkKh5dpxASuLMayYRV5PKOepgBpwZfRTiblJxhX3IfCx9G5Ql6zNElkpTYGjHM4rGvyvujKHnh0VtmlBrQRrA-FV3RMpy1elDWCTieVyIZE_sejTAfbom39OiZytu31dTEl5XZ8bDOktGsZiQv5fUeadhaB23DuUQuQt53Lq6Hjvisg9EIucJE5owEjeF1MKf8pv2wkQwseA'
    },
    {
        "id": 3,
        "name": 'Hueso de Goma Resistente',
        "category": 'Juguetes - Perros',
        "price": 25.50,
        "originalPrice": 0,
        "image": 'https://lh3.googleusercontent.com/aida-public/AB6AXuDYlSHN0ihN9GWy8Ixg5SkN_LmV3g4svzUUE8T1GOvttUR2Vzs_vVCnqfM5l9k2E2ap1YvC4JJEizq0Bo6GCqOWIGy7dNL_xLgSJpQEsRIXRgkQVgq4kDZuCd7sU9EIgIqIhtJ5VMX932AOOAkmZYQP-eoezJNLwtKtATXOnXC4x2kDkq0sjXHwyv4Gi6E-sk0p8cEnvQuW55KvNA48Nx2QI12xPdztXGq-tYBioWsSem8oW2TaUOSgv8yq7Ux2rKtYupITY2Cd7ZU',
        "description": 'Azul, Talla M'
    },
    {
        "id": 4,
        "name": 'Shampoo Antipulgas 400ml',
        "category": 'Higiene - General',
        "price": 32.00,
        "originalPrice": 38.00,
        "image": 'https://lh3.googleusercontent.com/aida-public/AB6AXuDsuVxadySIdQfFR3W32inefrZh7BcWmzCnla6FpYVAfCTeCGK5rTWsSYFf5FLwwGAtTUy33YNK46Ad-mhHQQKOGEgvog9YJ110IeNv59vwAICfqoqTdTY90vBUDkDIRqnbpyJqKXdt_9Pu94OybLQ7h26cCrkQPVGcFxoL1MXb1h6KA0P6mWDllW6YML62mBS5XdjzoPu54kFbc1n2aNYA3bSOi-PlbMN5m9WzwthdBPb2TCDB-GYZWpSwEomsvQkHlyWZXK4npd0',
        "badge": 'OFERTA',
        "description": 'Uso veterinario'
    },
    {
        "id": 5,
        "name": 'Spray Limpiador 300ml',
        "category": 'Higiene',
        "price": 28.90,
        "originalPrice": 0,
        "image": 'https://lh3.googleusercontent.com/aida-public/AB6AXuDsuVxadySIdQfFR3W32inefrZh7BcWmzCnla6FpYVAfCTeCGK5rTWsSYFf5FLwwGAtTUy33YNK46Ad-mhHQQKOGEgvog9YJ110IeNv59vwAICfqoqTdTY90vBUDkDIRqnbpyJqKXdt_9Pu94OybLQ7h26cCrkQPVGcFxoL1MXb1h6KA0P6mWDllW6YML62mBS5XdjzoPu54kFbc1n2aNYA3bSOi-PlbMN5m9WzwthdBPb2TCDB-GYZWpSwEomsvQkHlyWZXK4npd0'
    },
    {
        "id": 6,
        "name": 'Pack Premios DogChow',
        "category": 'Snacks',
        "price": 15.90,
        "originalPrice": 18.90,
        "image": 'https://lh3.googleusercontent.com/aida-public/AB6AXuB3Z1LMZsb74Tgm4Cdh1NMPZkSL8GB__pXbsiyqQiyL2faccfvknLupd0mIUrZUg21s-PggD_RMTBlxDgiiaiSilpfny7A0F9W31Cv2Em_QRo1wYXLs1RcxPnAMj4rJqn4YxlTUp3ac9Rqp-fRTxVYJI4jO__tswqLtZH-ucX4STrjSFuNuIZMutrtmJQAVPwMuOKrC7j6ng0L3vIc-tYRfzwfaLRnHRKhNPNhq48nkeD6ewUYIpuckVMjlRwX0CGiB8OcovDKBUA8',
        "badge": '-15%'
    },
    {
        "id": 7,
        "name": 'Collar Antipulgas Seresto',
        "category": 'Salud',
        "price": 145.00,
        "originalPrice": 0,
        "image": 'https://lh3.googleusercontent.com/aida-public/AB6AXuDYlSHN0ihN9GWy8Ixg5SkN_LmV3g4svzUUE8T1GOvttUR2Vzs_vVCnqfM5l9k2E2ap1YvC4JJEizq0Bo6GCqOWIGy7dNL_xLgSJpQEsRIXRgkQVgq4kDZuCd7sU9EIgIqIhtJ5VMX932AOOAkmZYQP-eoezJNLwtKtATXOnXC4x2kDkq0sjXHwyv4Gi6E-sk0p8cEnvQuW55KvNA48Nx2QI12xPdztXGq-tYBioWsSem8oW2TaUOSgv8yq7Ux2rKtYupITY2Cd7ZU'
    }
]
