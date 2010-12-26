BEGIN;
ALTER TABLE "posts_page" ADD COLUMN "order" integer NOT NULL DEFAULT 0;
ALTER TABLE "posts_page" ADD COLUMN "topmenu" boolean NOT NULL DEFAULT 0;
ALTER TABLE "posts_page" ADD COLUMN "linkbg" varchar(140) NOT NULL DEFAULT '';
ALTER TABLE "posts_page" ADD COLUMN "linken" varchar(140) NOT NULL DEFAULT '';
ALTER TABLE "posts_page" ADD COLUMN "linkfr" varchar(140) NOT NULL DEFAULT '';
COMMIT;