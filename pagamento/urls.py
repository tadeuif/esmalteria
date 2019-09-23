from django.urls import path
from .views import lista_de_pagamento,adicionar_pagamento,editar_pagamento,remover_pagamento
urlpatterns = [
    path('',lista_de_pagamento,name='lista_de_pagamento'),
    path('adicionar_pagamento/',adicionar_pagamento,name='adicionar_pagamento'),
    path('pagamento/editar_pagamento/<int:id>',editar_pagamento,name='editar_pagamento'),
    path('pagamento/remover_pagamento/<int:id>',remover_pagamento,name='remover_pagamento')
    
]
