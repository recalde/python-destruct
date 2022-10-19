CREATE TABLE credit.chase_transaction (
	chase_transaction_key int8 NOT NULL GENERATED ALWAYS AS IDENTITY,
	transaction_date varchar NULL,
	post_date varchar NULL,
	description varchar NULL,
	category varchar NULL,
	"type" varchar NULL,
	amount numeric NULL,
	memo varchar NULL,
	CONSTRAINT chase_transaction_pk PRIMARY KEY (chase_transaction_key)
);