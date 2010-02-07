alter table core_presentation add column `embedded_video` text null;
alter table core_presentation add column `embedded_pdf` text null;
alter table core_presentation add column `order` integer default 100;
