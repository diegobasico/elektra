CREATE TABLE IF NOT EXISTS "entidades" (
	"id" INTEGER NOT NULL UNIQUE,
	"nombre" TEXT,
	PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "empresas" (
	"id" INTEGER NOT NULL UNIQUE,
	"nombre" TEXT,
	"ruc" INTEGER,
	PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "consorcios" (
	"id" INTEGER NOT NULL UNIQUE,
	"nombre" TEXT,
	PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "consorcios_empresas_m2m" (
	"id" INTEGER NOT NULL UNIQUE,
	"consorcio_id" INTEGER,
	"empresa_id" INTEGER,
	PRIMARY KEY("id"),
	FOREIGN KEY ("consorcio_id") REFERENCES "consorcios"("id")
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY ("empresa_id") REFERENCES "empresas"("id")
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS "obras" (
	"id" INTEGER NOT NULL UNIQUE,
	"nombre" TEXT,
	"consorcio_id" INTEGER,
	"empresa_id" INTEGER,
	"monto" REAL,
	"entidad_id" INTEGER,
	"fecha_contrato" TEXT,
	"fecha_recepción" TEXT,
	PRIMARY KEY("id"),
	FOREIGN KEY ("consorcio_id") REFERENCES "consorcios"("id")
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY ("empresa_id") REFERENCES "empresas"("id")
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY ("entidad_id") REFERENCES "entidades"("id")
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS "documentos" (
	"id" INTEGER NOT NULL UNIQUE,
	"nombre" TEXT,
	"obra_id" INTEGER,
	"tipo_id" INTEGER,
	"archivo" BLOB,
	PRIMARY KEY("id"),
	FOREIGN KEY ("obra_id") REFERENCES "obras"("id")
	ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY ("tipo_id") REFERENCES "tipos_documento"("id")
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS "tipos_documento" (
	"id" INTEGER NOT NULL UNIQUE,
	"tipo" TEXT,
	PRIMARY KEY("id")
);
