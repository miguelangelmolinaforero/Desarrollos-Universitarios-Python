ALTER TABLE PEDIDOS
ADD CONSTRAINT FK_cod_cliente
FOREIGN KEY (cod_cliente) 
REFERENCES CLIENTES(cod_cliente);
