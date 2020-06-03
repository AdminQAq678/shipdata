use [ShipData]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[insertNew]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[insertNew]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[updateSCI]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[updateSCI]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[deleteSCI]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[deleteSCI]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[MainTP]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[MainTP]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[MainTU]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[MainTU]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[DelMainTain]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[DelMainTain]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[updateFeeState]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[updateFeeState]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[InsertYingYun]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[InsertYingYun]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[UpdateYingYun]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[UpdateYingYun]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[DeleteYingYun]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[DeleteYingYun]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[InsertYingYun1]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[InsertYingYun1]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[UpdateYingYun1]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[UpdateYingYun1]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[DeleteProve]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[DeleteProve]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[updateLineFee]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[updateLineFee]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[InsertYingYun6]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[InsertYingYun6]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[UpdateYingYun6]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[UpdateYingYun6]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[DeleteStationP]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[DeleteStationP]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[insertFeeState]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[insertFeeState]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[InsertYingYunSP]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[InsertYingYunSP]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[UpdateSP]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[UpdateSP]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[DeleteSafteLP]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[DeleteSafteLP]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[InsertRC]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[InsertRC]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[UpdateRC]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[UpdateRC]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[DeleteRC]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[DeleteRC]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[InsertYingYun2]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[InsertYingYun2]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[UpdateYingYun2]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[UpdateYingYun2]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[DeleteLoadLine]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[DeleteLoadLine]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[DeleteDP]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[DeleteDP]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[insertYingYun3]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[insertYingYun3]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[UpdateYingYun3]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[UpdateYingYun3]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[InsertYingYun4]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[InsertYingYun4]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[UpdateYingYun4]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[UpdateYingYun4]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[DeletePOP]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[DeletePOP]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[InsertYingYun5]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[InsertYingYun5]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[UpdateYingYun5]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[UpdateYingYun5]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[DeleteShiHang]') and OBJECTPROPERTY(id, N'IsTrigger') = 1)
drop trigger [dbo].[DeleteShiHang]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[FeeVIEW]') and OBJECTPROPERTY(id, N'IsView') = 1)
drop view [dbo].[FeeVIEW]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[ShipProveVIEW]') and OBJECTPROPERTY(id, N'IsView') = 1)
drop view [dbo].[ShipProveVIEW]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[中间检验处理历史表]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[中间检验处理历史表]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[危险品证书处理历史表]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[危险品证书处理历史表]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[各证书有效期]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[各证书有效期]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[国籍证书处理历史表]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[国籍证书处理历史表]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[坞内检验处理历史表]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[坞内检验处理历史表]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[安全检查处理历史表]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[安全检查处理历史表]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[安全检查通知书]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[安全检查通知书]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[年度检验处理历史表]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[年度检验处理历史表]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[检修证明]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[检修证明]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[水运费有效期]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[水运费有效期]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[水运费记录表]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[水运费记录表]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[油污证书处理历史表]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[油污证书处理历史表]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[港澳航线船舶营运证]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[港澳航线船舶营运证]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[港澳证明处理历史表]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[港澳证明处理历史表]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[特别检验处理历史表]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[特别检验处理历史表]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[系统参数表]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[系统参数表]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[系统用户表]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[系统用户表]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[航行港澳船舶证明书]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[航行港澳船舶证明书]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[航道费有效期]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[航道费有效期]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[航道费记录表]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[航道费记录表]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[船员档案]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[船员档案]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[船舶共有情况]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[船舶共有情况]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[船舶国籍证书]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[船舶国籍证书]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[船舶所有权登记证书]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[船舶所有权登记证书]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[船舶最低安全配员证书]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[船舶最低安全配员证书]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[船舶电台执照]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[船舶电台执照]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[船舶相片]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[船舶相片]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[船舶载重线证书]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[船舶载重线证书]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[船舶运载危险品证书]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[船舶运载危险品证书]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[船舶防止油污证书]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[船舶防止油污证书]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[营运证处理历史表]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[营运证处理历史表]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[螺旋桨尾轴检验处理历史表]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[螺旋桨尾轴检验处理历史表]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[货船适航证书]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[货船适航证书]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[费用设置表]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[费用设置表]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[载重线证书处理历史表]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[载重线证书处理历史表]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[适航证书处理历史表]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[适航证书处理历史表]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[配员证书处理历史表]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[配员证书处理历史表]
GO

if exists (select * from dbo.sysobjects where id = object_id(N'[dbo].[锅炉检验处理历史表]') and OBJECTPROPERTY(id, N'IsUserTable') = 1)
drop table [dbo].[锅炉检验处理历史表]
GO

CREATE TABLE [dbo].[中间检验处理历史表] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[办理日期] [datetime] NOT NULL ,
	[办理人] [varchar] (10) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书有效期至] [datetime] NOT NULL ,
	[业务办理情况] [varchar] (100) COLLATE Chinese_PRC_CI_AS NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[危险品证书处理历史表] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[办理日期] [datetime] NOT NULL ,
	[办理人] [varchar] (10) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书有效期至] [datetime] NOT NULL ,
	[业务办理情况] [varchar] (100) COLLATE Chinese_PRC_CI_AS NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[各证书有效期] (
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书名] [varchar] (18) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书有效期至] [datetime] NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[国籍证书处理历史表] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[办理日期] [datetime] NOT NULL ,
	[办理人] [varchar] (10) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书有效期至] [datetime] NOT NULL ,
	[业务办理情况] [varchar] (100) COLLATE Chinese_PRC_CI_AS NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[坞内检验处理历史表] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[办理日期] [datetime] NOT NULL ,
	[办理人] [varchar] (10) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书有效期至] [datetime] NOT NULL ,
	[业务办理情况] [varchar] (100) COLLATE Chinese_PRC_CI_AS NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[安全检查处理历史表] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NULL ,
	[业务办理人] [varchar] (30) COLLATE Chinese_PRC_CI_AS NULL ,
	[检查日期] [datetime] NULL ,
	[下次检查日期] [datetime] NULL ,
	[检查情况] [varchar] (500) COLLATE Chinese_PRC_CI_AS NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[安全检查通知书] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[船舶所有人] [varchar] (30) COLLATE Chinese_PRC_CI_AS NULL ,
	[船舶种类] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[总吨] [decimal](18, 2) NULL ,
	[建成日期] [datetime] NULL ,
	[检查日期] [datetime] NULL ,
	[下次检查日期] [datetime] NULL ,
	[检查情况] [varchar] (500) COLLATE Chinese_PRC_CI_AS NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[年度检验处理历史表] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[办理日期] [datetime] NOT NULL ,
	[办理人] [varchar] (10) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书有效期至] [datetime] NOT NULL ,
	[业务办理情况] [varchar] (100) COLLATE Chinese_PRC_CI_AS NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[检修证明] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[检修类型] [varchar] (30) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[签发时间] [datetime] NOT NULL ,
	[检修证明编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[下次检修时间] [datetime] NOT NULL ,
	[筏站名称] [varchar] (50) COLLATE Chinese_PRC_CI_AS NULL ,
	[是否有效] [varchar] (4) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[检修情况说明] [varchar] (300) COLLATE Chinese_PRC_CI_AS NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[水运费有效期] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[费用有效期] [datetime] NOT NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[水运费记录表] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[水运费用] [money] NOT NULL ,
	[交付日期] [datetime] NOT NULL ,
	[缴纳月数] [int] NULL ,
	[费用有效期] [datetime] NOT NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[油污证书处理历史表] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[办理日期] [datetime] NOT NULL ,
	[办理人] [varchar] (10) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书有效期至] [datetime] NOT NULL ,
	[业务办理情况] [varchar] (100) COLLATE Chinese_PRC_CI_AS NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[港澳航线船舶营运证] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[载客定额] [int] NULL ,
	[载货定额] [decimal](18, 2) NULL ,
	[经济性质] [varchar] (30) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[船舶经营人] [varchar] (30) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[批准机关] [varchar] (30) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[批准文号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[客运航线] [varchar] (50) COLLATE Chinese_PRC_CI_AS NULL ,
	[货运航线] [varchar] (150) COLLATE Chinese_PRC_CI_AS NULL ,
	[发证日期] [datetime] NOT NULL ,
	[有效日期] [datetime] NOT NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[港澳证明处理历史表] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[办理日期] [datetime] NOT NULL ,
	[办理人] [varchar] (10) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书有效期至] [datetime] NOT NULL ,
	[业务办理情况] [varchar] (100) COLLATE Chinese_PRC_CI_AS NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[特别检验处理历史表] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[办理日期] [datetime] NOT NULL ,
	[办理人] [varchar] (10) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书有效期至] [datetime] NOT NULL ,
	[业务办理情况] [varchar] (100) COLLATE Chinese_PRC_CI_AS NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[系统参数表] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[参数名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[取值] [int] NOT NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[系统用户表] (
	[用户ID] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[密码] [varchar] (100) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[权限] [varchar] (50) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[员工姓名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NULL ,
	[联系电话] [varchar] (50) COLLATE Chinese_PRC_CI_AS NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[航行港澳船舶证明书] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船舶名称] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[船员定额] [int] NOT NULL ,
	[船舶种类] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[载重吨位] [decimal](18, 2) NOT NULL ,
	[船籍港] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[所属单位] [varchar] (30) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[航行有效期] [datetime] NOT NULL ,
	[批复文号] [varchar] (25) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[签发机关] [varchar] (30) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[发证日期] [datetime] NOT NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[航道费有效期] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[费用有效期] [datetime] NOT NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[航道费记录表] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[航道费用] [money] NOT NULL ,
	[交付日期] [datetime] NOT NULL ,
	[缴纳月数] [int] NULL ,
	[费用有效期] [datetime] NOT NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[船员档案] (
	[编号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (30) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[姓名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[姓名拼音] [varchar] (30) COLLATE Chinese_PRC_CI_AS NULL ,
	[性别] [varchar] (2) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[身份证号码] [varchar] (18) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[出生地] [varchar] (30) COLLATE Chinese_PRC_CI_AS NULL ,
	[相片] [image] NULL ,
	[海员证号码] [varchar] (30) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[服务簿号码] [varchar] (30) COLLATE Chinese_PRC_CI_AS NULL ,
	[海员证到期日] [datetime] NOT NULL ,
	[文化程度] [char] (10) COLLATE Chinese_PRC_CI_AS NULL ,
	[家庭联系地址] [varchar] (50) COLLATE Chinese_PRC_CI_AS NULL ,
	[联系电话] [varchar] (30) COLLATE Chinese_PRC_CI_AS NULL ,
	[毕业学校] [varchar] (50) COLLATE Chinese_PRC_CI_AS NULL ,
	[专业] [varchar] (30) COLLATE Chinese_PRC_CI_AS NULL ,
	[毕业证编号] [varchar] (30) COLLATE Chinese_PRC_CI_AS NULL ,
	[毕业时间] [datetime] NULL ,
	[合同相片] [image] NULL ,
	[适任证类别等级职务] [varchar] (30) COLLATE Chinese_PRC_CI_AS NULL ,
	[适任证书号码] [varchar] (30) COLLATE Chinese_PRC_CI_AS NULL ,
	[适任证书到期日] [datetime] NULL ,
	[适任证发证机关] [varchar] (30) COLLATE Chinese_PRC_CI_AS NULL ,
	[GMDSS适任证书号码] [varchar] (30) COLLATE Chinese_PRC_CI_AS NULL ,
	[GMDSS适任证发证日期] [datetime] NULL ,
	[GMDSS适任证书到期日] [datetime] NULL ,
	[健康证号码] [varchar] (30) COLLATE Chinese_PRC_CI_AS NULL ,
	[健康证发证日期] [datetime] NULL ,
	[健康证书到期日] [datetime] NULL ,
	[货物处理课程证明书号码] [varchar] (30) COLLATE Chinese_PRC_CI_AS NULL ,
	[货物处理课程证明发证日期] [datetime] NULL ,
	[货物处理课程证明书到期日] [datetime] NULL ,
	[工程监督员课程证明号码] [varchar] (30) COLLATE Chinese_PRC_CI_AS NULL ,
	[工程监督员课程证明发证日期] [datetime] NULL ,
	[工程监督员课程证明到期日] [datetime] NULL 
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

CREATE TABLE [dbo].[船舶共有情况] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[股东名] [varchar] (30) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[股份] [decimal](18, 0) NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[船舶国籍证书] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[曾用名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NULL ,
	[证书编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书有效期] [datetime] NOT NULL ,
	[取得所有权日期] [datetime] NOT NULL ,
	[签发日期] [datetime] NOT NULL ,
	[发证机关及其编号] [varchar] (50) COLLATE Chinese_PRC_CI_AS NOT NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[船舶所有权登记证书] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[登记号码] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[初次登记号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[曾用名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NULL ,
	[船籍港] [varchar] (20) COLLATE Chinese_PRC_CI_AS NULL ,
	[原船籍港] [varchar] (20) COLLATE Chinese_PRC_CI_AS NULL ,
	[船舶呼号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NULL ,
	[IMO编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NULL ,
	[船舶种类] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[船体材料] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[造船地点] [varchar] (50) COLLATE Chinese_PRC_CI_AS NULL ,
	[建成日期] [datetime] NOT NULL ,
	[船舶价值] [money] NULL ,
	[总长] [decimal](18, 2) NOT NULL ,
	[型宽] [decimal](18, 2) NOT NULL ,
	[型深] [decimal](18, 2) NOT NULL ,
	[总吨] [decimal](18, 2) NOT NULL ,
	[载重] [decimal](18, 0) NULL ,
	[净吨] [decimal](18, 2) NOT NULL ,
	[主机种类] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[主机数目] [int] NOT NULL ,
	[功率] [decimal](18, 2) NOT NULL ,
	[推进器种类] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[推进器数目] [int] NOT NULL ,
	[船舶所有人] [varchar] (30) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[船舶所有人地址] [varchar] (100) COLLATE Chinese_PRC_CI_AS NULL ,
	[法定代表人姓名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[取得所有权日期] [datetime] NULL ,
	[发证机关] [varchar] (30) COLLATE Chinese_PRC_CI_AS NULL ,
	[编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NULL ,
	[发证日期] [datetime] NOT NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[船舶最低安全配员证书] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[船舶种类] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[船籍港] [varchar] (30) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[签发日期] [datetime] NOT NULL ,
	[发证机关] [varchar] (30) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书有效期至] [datetime] NOT NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[船舶电台执照] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[呼号] [varchar] (30) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[隶属单位] [varchar] (30) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[公众通信类别] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[签发日期] [datetime] NOT NULL ,
	[有效期至] [datetime] NOT NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[船舶相片] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[船舶相片] [image] NULL ,
	[相片类型] [char] (10) COLLATE Chinese_PRC_CI_AS NULL 
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

CREATE TABLE [dbo].[船舶载重线证书] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[船检登记号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[船长] [decimal](18, 2) NULL ,
	[计算型深] [decimal](18, 2) NULL ,
	[发证日期] [datetime] NOT NULL ,
	[有效日期] [datetime] NOT NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[船舶运载危险品证书] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[船检登记号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[发证日期] [datetime] NOT NULL ,
	[证书有效期] [datetime] NOT NULL ,
	[发证机关] [varchar] (20) COLLATE Chinese_PRC_CI_AS NULL ,
	[危险品种类] [varchar] (100) COLLATE Chinese_PRC_CI_AS NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[船舶防止油污证书] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[船检登记号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[船舶种类] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[建造日期] [datetime] NOT NULL ,
	[证书有效期] [datetime] NOT NULL ,
	[发证日期] [datetime] NOT NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[营运证处理历史表] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[办理日期] [datetime] NOT NULL ,
	[办理人] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书有效期至] [datetime] NOT NULL ,
	[业务办理情况] [varchar] (100) COLLATE Chinese_PRC_CI_AS NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[螺旋桨尾轴检验处理历史表] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[办理日期] [datetime] NOT NULL ,
	[办理人] [varchar] (10) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书有效期至] [datetime] NOT NULL ,
	[业务办理情况] [varchar] (100) COLLATE Chinese_PRC_CI_AS NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[货船适航证书] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[船检登记号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书有效期] [datetime] NOT NULL ,
	[年度检验日期] [datetime] NULL ,
	[中间检验日期] [datetime] NULL ,
	[特别检验日期] [datetime] NULL ,
	[坞内检验日期] [datetime] NULL ,
	[螺旋桨尾轴检验日期] [datetime] NULL ,
	[锅炉检验日期] [datetime] NULL ,
	[航区航线] [varchar] (200) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[发证日期] [datetime] NOT NULL ,
	[发证单位] [varchar] (30) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[主任验船师] [varchar] (10) COLLATE Chinese_PRC_CI_AS NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[费用设置表] (
	[费用名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[计算类型] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[月吨] [decimal](18, 2) NULL ,
	[季吨] [decimal](18, 2) NULL ,
	[年吨] [decimal](18, 2) NULL ,
	[过期月吨] [decimal](18, 2) NULL ,
	[过期季吨] [decimal](18, 2) NULL ,
	[过期年吨] [decimal](18, 2) NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[载重线证书处理历史表] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[办理日期] [datetime] NOT NULL ,
	[办理人] [varchar] (10) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书有效期至] [datetime] NOT NULL ,
	[业务办理情况] [varchar] (100) COLLATE Chinese_PRC_CI_AS NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[适航证书处理历史表] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[办理日期] [datetime] NOT NULL ,
	[办理人] [varchar] (10) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书有效期至] [datetime] NOT NULL ,
	[业务办理情况] [varchar] (100) COLLATE Chinese_PRC_CI_AS NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[配员证书处理历史表] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[办理日期] [datetime] NOT NULL ,
	[办理人] [varchar] (10) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书有效期至] [datetime] NOT NULL ,
	[业务办理情况] [varchar] (100) COLLATE Chinese_PRC_CI_AS NULL 
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[锅炉检验处理历史表] (
	[序号] [int] IDENTITY (1, 1) NOT NULL ,
	[船名] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书编号] [varchar] (20) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[办理日期] [datetime] NOT NULL ,
	[办理人] [varchar] (10) COLLATE Chinese_PRC_CI_AS NOT NULL ,
	[证书有效期至] [datetime] NOT NULL ,
	[业务办理情况] [varchar] (100) COLLATE Chinese_PRC_CI_AS NULL 
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[各证书有效期] ADD 
	CONSTRAINT [PK_各证书有效期] PRIMARY KEY  CLUSTERED 
	(
		[船名],
		[证书名]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[安全检查通知书] ADD 
	CONSTRAINT [PK_安全检查通知书] PRIMARY KEY  CLUSTERED 
	(
		[船名]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[检修证明] ADD 
	CONSTRAINT [PK_检修证明] PRIMARY KEY  CLUSTERED 
	(
		[船名]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[港澳航线船舶营运证] ADD 
	CONSTRAINT [PK_港澳航线船舶营运证] PRIMARY KEY  CLUSTERED 
	(
		[船名]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[系统用户表] ADD 
	CONSTRAINT [PK_系统用户表] PRIMARY KEY  CLUSTERED 
	(
		[用户ID]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[航行港澳船舶证明书] ADD 
	CONSTRAINT [PK_航行港澳船舶证明书] PRIMARY KEY  CLUSTERED 
	(
		[船舶名称]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[航道费有效期] ADD 
	CONSTRAINT [PK_航道费有效期] PRIMARY KEY  CLUSTERED 
	(
		[船名]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[船员档案] ADD 
	CONSTRAINT [PK_船员档案] PRIMARY KEY  CLUSTERED 
	(
		[船名],
		[姓名]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[船舶共有情况] ADD 
	CONSTRAINT [PK_船舶共有情况] PRIMARY KEY  CLUSTERED 
	(
		[船名],
		[股东名]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[船舶国籍证书] ADD 
	CONSTRAINT [PK_船舶国籍证书] PRIMARY KEY  CLUSTERED 
	(
		[船名]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[船舶所有权登记证书] ADD 
	CONSTRAINT [PK_船舶所有权登记证书] PRIMARY KEY  CLUSTERED 
	(
		[船名]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[船舶最低安全配员证书] ADD 
	CONSTRAINT [PK_船舶最低安全配员证书] PRIMARY KEY  CLUSTERED 
	(
		[船名]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[船舶电台执照] ADD 
	CONSTRAINT [PK_船舶电台执照] PRIMARY KEY  CLUSTERED 
	(
		[船名]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[船舶相片] ADD 
	CONSTRAINT [PK_船舶相片] PRIMARY KEY  CLUSTERED 
	(
		[船名]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[船舶载重线证书] ADD 
	CONSTRAINT [PK_船舶载重线证书] PRIMARY KEY  CLUSTERED 
	(
		[船名]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[船舶运载危险品证书] ADD 
	CONSTRAINT [PK_船舶运载危险品证书] PRIMARY KEY  CLUSTERED 
	(
		[船名]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[船舶防止油污证书] ADD 
	CONSTRAINT [PK_船舶防止油污证书] PRIMARY KEY  CLUSTERED 
	(
		[船名]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[货船适航证书] ADD 
	CONSTRAINT [PK_货船适航证书] PRIMARY KEY  CLUSTERED 
	(
		[船名]
	)  ON [PRIMARY] 
GO

ALTER TABLE [dbo].[费用设置表] ADD 
	CONSTRAINT [DF_费用设置表_月吨] DEFAULT (0) FOR [月吨],
	CONSTRAINT [DF_费用设置表_季吨] DEFAULT (0) FOR [季吨],
	CONSTRAINT [DF_费用设置表_年吨] DEFAULT (0) FOR [年吨],
	CONSTRAINT [DF_费用设置表_过期月吨] DEFAULT (0) FOR [过期月吨],
	CONSTRAINT [DF_费用设置表_过期季吨] DEFAULT (0) FOR [过期季吨],
	CONSTRAINT [DF_费用设置表_过期年吨] DEFAULT (0) FOR [过期年吨],
	CONSTRAINT [PK_费用设置表] PRIMARY KEY  CLUSTERED 
	(
		[费用名]
	)  ON [PRIMARY] 
GO

SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS ON 
GO

CREATE VIEW dbo.FeeVIEW
AS
SELECT dbo.水运费有效期.费用有效期 AS 水运费有效期至, 
      dbo.航道费有效期.费用有效期 AS 航道费有效期至, dbo.船舶所有权登记证书.船名, 
      dbo.船舶所有权登记证书.登记号码, dbo.船舶所有权登记证书.建成日期, 
      dbo.船舶所有权登记证书.总长, dbo.船舶所有权登记证书.型宽, 
      dbo.船舶所有权登记证书.型深, dbo.船舶所有权登记证书.总吨, 
      dbo.船舶所有权登记证书.载重, dbo.船舶所有权登记证书.净吨, 
      dbo.船舶所有权登记证书.船舶所有人, dbo.船舶所有权登记证书.船舶所有人地址, 
      dbo.船舶所有权登记证书.法定代表人姓名
FROM dbo.船舶所有权登记证书 INNER JOIN
      dbo.水运费有效期 ON 
      dbo.船舶所有权登记证书.船名 = dbo.水运费有效期.船名 INNER JOIN
      dbo.航道费有效期 ON dbo.船舶所有权登记证书.船名 = dbo.航道费有效期.船名

GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS ON 
GO

CREATE VIEW dbo.ShipProveVIEW
AS
SELECT dbo.各证书有效期.*, dbo.船舶所有权登记证书.船舶所有人地址, 
      dbo.船舶所有权登记证书.法定代表人姓名
FROM dbo.各证书有效期 INNER JOIN
      dbo.船舶所有权登记证书 ON dbo.各证书有效期.船名 = dbo.船舶所有权登记证书.船名

GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER insertNew ON [dbo].[安全检查通知书] 
FOR INSERT
AS
insert into 各证书有效期( 船名,证书名,证书有效期至) 
         select 船名,'安全检查通知书',下次检查日期 from inserted 
GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER updateSCI ON [dbo].[安全检查通知书] 
FOR UPDATE 
AS
Update 各证书有效期 set 证书有效期至=(select inserted .下次检查日期 from inserted, 各证书有效期  
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='安全检查通知书') 
 from 各证书有效期,inserted
 where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='安全检查通知书'
GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER deleteSCI ON [dbo].[安全检查通知书] 
FOR DELETE 
AS
DELETE FROM 各证书有效期 where 各证书有效期.船名= (select 船名 from deleted) and 各证书有效期.证书名='安全检查通知书'
GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER MainTP ON [dbo].[检修证明] 
FOR INSERT
AS
insert into 各证书有效期( 船名,证书名,证书有效期至) 
         select 船名,'检修证明',下次检修时间 from inserted
GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER MainTU ON [dbo].[检修证明] 
FOR UPDATE
AS
Update 各证书有效期 set 证书有效期至=(select inserted .下次检修时间 from inserted, 各证书有效期  
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='检修证明') 
 from 各证书有效期,inserted
 where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='检修证明'
GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER DelMainTain ON [dbo].[检修证明] 
FOR DELETE
AS
DELETE FROM 各证书有效期 where 各证书有效期.船名= (select 船名 from deleted) and 各证书有效期.证书名='检修证明'

GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER updateFeeState ON dbo.水运费记录表 
FOR INSERT
AS
update 水运费有效期 set 费用有效期=(select 费用有效期 from inserted)
where 船名 in (select 船名 from inserted)

GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER InsertYingYun ON dbo.港澳航线船舶营运证 
FOR INSERT
AS
insert into 各证书有效期( 船名,证书名,证书有效期至) 
         select 船名,'港澳营运证',有效日期 from inserted

GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER UpdateYingYun ON dbo.港澳航线船舶营运证 
FOR UPDATE
AS
Update 各证书有效期 set 证书有效期至=(select inserted .有效日期 from inserted, 各证书有效期  where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='港澳营运证') 
 from 各证书有效期,inserted
 where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='港澳营运证'

GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER DeleteYingYun ON [dbo].[港澳航线船舶营运证] 
FOR DELETE
AS
DELETE FROM 各证书有效期 where 各证书有效期.船名= (select 船名 from deleted) and 各证书有效期.证书名='港澳营运证'
GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER InsertYingYun1 ON dbo.航行港澳船舶证明书 
FOR INSERT
AS
insert into 各证书有效期( 船名,证书名,证书有效期至) 
         select 船舶名称,'港澳证明书',航行有效期 from inserted

GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER UpdateYingYun1 ON dbo.航行港澳船舶证明书 
FOR UPDATE
AS
Update 各证书有效期 set 证书有效期至=(select inserted .航行有效期 from inserted, 各证书有效期  
where 各证书有效期.船名=inserted.船舶名称 and 各证书有效期.证书名='港澳证明书') 
 from 各证书有效期,inserted
 where 各证书有效期.船名=inserted.船舶名称 and 各证书有效期.证书名='港澳证明书'

GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER DeleteProve ON [dbo].[航行港澳船舶证明书] 
FOR DELETE
AS
DELETE FROM 各证书有效期 where 各证书有效期.船名= (select 船舶名称 from deleted) and 各证书有效期.证书名='港澳证明书'
GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER updateLineFee  ON dbo.航道费记录表 
FOR INSERT
AS
update 航道费有效期 set 费用有效期=(select 费用有效期 from inserted)
where 船名 in (select 船名 from inserted)

GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER InsertYingYun6 ON [dbo].[船舶国籍证书] 
FOR INSERT
AS
insert into 各证书有效期( 船名,证书名,证书有效期至) 
         select 船名,'船舶国籍证书',证书有效期 from inserted 
GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER UpdateYingYun6 ON [dbo].[船舶国籍证书] 
FOR UPDATE 
AS
Update 各证书有效期 set 证书有效期至=(select inserted .证书有效期 from inserted, 各证书有效期  
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='船舶国籍证书') 
 from 各证书有效期,inserted
 where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='船舶国籍证书'


GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER DeleteStationP ON [dbo].[船舶国籍证书] 
FOR DELETE
AS
DELETE FROM 各证书有效期 where 各证书有效期.船名= (select 船名 from deleted) and 各证书有效期.证书名='船舶国籍证书'
GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER insertFeeState ON dbo.船舶所有权登记证书 
FOR INSERT
AS
insert into 水运费有效期(船名,费用有效期)
select 船名,Convert(VARCHAR(30),getdate(),11) from inserted
insert into 航道费有效期(船名,费用有效期)
select 船名,Convert(VARCHAR(30),getdate(),11) from inserted


GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER InsertYingYunSP ON [dbo].[船舶最低安全配员证书] 
FOR INSERT
AS
insert into 各证书有效期( 船名,证书名,证书有效期至) 
         select 船名,'最低安全配员证',证书有效期至 from inserted 
GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER UpdateSP ON [dbo].[船舶最低安全配员证书] 
FOR  UPDATE
AS
Update 各证书有效期 set 证书有效期至=(select inserted .证书有效期至 from inserted, 各证书有效期  
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='最低安全配员证') 
 from 各证书有效期,inserted
 where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='最低安全配员证'
GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER DeleteSafteLP ON [dbo].[船舶最低安全配员证书] 
FOR DELETE
AS
DELETE FROM 各证书有效期 where 各证书有效期.船名= (select 船名 from deleted) and 各证书有效期.证书名='最低安全配员证'
GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER InsertRC ON dbo.船舶电台执照 
FOR INSERT
AS
insert into 各证书有效期( 船名,证书名,证书有效期至) 
         select 船名,'船舶电台执照',有效期至 from inserted

GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER UpdateRC ON dbo.船舶电台执照 
FOR UPDATE
AS
Update 各证书有效期 set 证书有效期至=(select inserted .有效期至 from inserted, 各证书有效期  
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='船舶电台执照') 
 from 各证书有效期,inserted
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='船舶电台执照'

GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER DeleteRC ON dbo.船舶电台执照 
FOR DELETE
AS
DELETE FROM 各证书有效期 where 各证书有效期.船名= (select 船名 from deleted) and 各证书有效期.证书名='船舶电台执照'

GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER InsertYingYun2 ON dbo.船舶载重线证书 
FOR INSERT
AS
insert into 各证书有效期( 船名,证书名,证书有效期至) 
         select 船名,'载重线证书',有效日期 from inserted

GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER UpdateYingYun2 ON dbo.船舶载重线证书 
FOR UPDATE
AS
Update 各证书有效期 set 证书有效期至=(select inserted .有效日期 from inserted, 各证书有效期  
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='载重线证书') 
 from 各证书有效期,inserted
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='载重线证书'

GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER DeleteLoadLine ON [dbo].[船舶载重线证书] 
FOR DELETE
AS
DELETE FROM 各证书有效期 where 各证书有效期.船名= (select 船名 from deleted) and 各证书有效期.证书名='载重线证书'
GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER DeleteDP ON [dbo].[船舶运载危险品证书] 
FOR DELETE
AS
DELETE FROM 各证书有效期 where 各证书有效期.船名= (select 船名 from deleted) and 各证书有效期.证书名='危险品证书'
GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER insertYingYun3 ON dbo.船舶运载危险品证书 
FOR INSERT
AS
insert into 各证书有效期( 船名,证书名,证书有效期至) 
         select 船名,'危险品证书',证书有效期 from inserted

GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER UpdateYingYun3 ON dbo.船舶运载危险品证书 
FOR UPDATE
AS
Update 各证书有效期 set 证书有效期至=(select inserted .证书有效期 from inserted, 各证书有效期  
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='危险品证书') 
 from 各证书有效期,inserted
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='危险品证书'

GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER InsertYingYun4 ON dbo.船舶防止油污证书 
FOR INSERT
AS
insert into 各证书有效期( 船名,证书名,证书有效期至) 
         select 船名,'防污证书',证书有效期 from inserted

GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER UpdateYingYun4 ON dbo.船舶防止油污证书 
FOR UPDATE
AS
Update 各证书有效期 set 证书有效期至=(select inserted .证书有效期 from inserted, 各证书有效期  
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='防污证书') 
 from 各证书有效期,inserted
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='防污证书'

GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER DeletePOP ON [dbo].[船舶防止油污证书] 
FOR DELETE
AS
DELETE FROM 各证书有效期 where 各证书有效期.船名= (select 船名 from deleted) and 各证书有效期.证书名='防污证书'
GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER InsertYingYun5 ON dbo.货船适航证书 
FOR INSERT
AS
insert into 各证书有效期( 船名,证书名,证书有效期至) 
         select 船名,'适航证书',证书有效期 from inserted 
insert into 各证书有效期( 船名,证书名,证书有效期至) 
         select 船名,'年度检验',年度检验日期 from inserted 
insert into 各证书有效期( 船名,证书名,证书有效期至) 
         select 船名,'中间检验',中间检验日期 from inserted 
insert into 各证书有效期( 船名,证书名,证书有效期至) 
         select 船名,'特别检验',特别检验日期 from inserted 
insert into 各证书有效期( 船名,证书名,证书有效期至) 
         select 船名,'坞内检验',坞内检验日期 from inserted 
insert into 各证书有效期( 船名,证书名,证书有效期至) 
         select 船名,'螺旋桨尾轴检验',螺旋桨尾轴检验日期 from inserted 
insert into 各证书有效期( 船名,证书名,证书有效期至) 
         select 船名,'锅炉检验',锅炉检验日期 from inserted

GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER ON 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER UpdateYingYun5 ON dbo.货船适航证书 
FOR UPDATE
AS
IF UPDATE ( 证书有效期 )
   BEGIN
Update 各证书有效期 set 证书有效期至=(select inserted .证书有效期 from inserted, 各证书有效期  
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='适航证书') 
 from 各证书有效期,inserted
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='适航证书'
   END

IF UPDATE ( 年度检验日期 ) 
   BEGIN
Update 各证书有效期 set 证书有效期至=(select inserted .年度检验日期 from inserted, 各证书有效期  
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='年度检验') 
 from 各证书有效期,inserted
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='年度检验'
   END

IF UPDATE ( 中间检验日期 ) 
   BEGIN
Update 各证书有效期 set 证书有效期至=(select inserted .中间检验日期 from inserted, 各证书有效期  
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='中间检验') 
 from 各证书有效期,inserted
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='中间检验'
   END  

IF UPDATE ( 特别检验日期 ) 
   BEGIN
Update 各证书有效期 set 证书有效期至=(select inserted .特别检验日期 from inserted, 各证书有效期  
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='特别检验') 
 from 各证书有效期,inserted
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='特别检验'
   END  

IF UPDATE ( 坞内检验日期 ) 
   BEGIN
Update 各证书有效期 set 证书有效期至=(select inserted .坞内检验日期 from inserted, 各证书有效期  
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='坞内检验') 
 from 各证书有效期,inserted
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='坞内检验'
   END  

IF UPDATE ( 螺旋桨尾轴检验日期 ) 
   BEGIN
Update 各证书有效期 set 证书有效期至=(select inserted .螺旋桨尾轴检验日期 from inserted, 各证书有效期  
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='螺旋桨尾轴检验') 
 from 各证书有效期,inserted
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='螺旋桨尾轴检验'
   END  

IF UPDATE ( 锅炉检验日期 ) 
   BEGIN
Update 各证书有效期 set 证书有效期至=(select inserted .锅炉检验日期 from inserted, 各证书有效期  
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='锅炉检验') 
 from 各证书有效期,inserted
where 各证书有效期.船名=inserted.船名 and 各证书有效期.证书名='锅炉检验'
   END

GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

CREATE TRIGGER DeleteShiHang ON [dbo].[货船适航证书] 
FOR DELETE
AS
begin
DELETE FROM 各证书有效期 where 各证书有效期.船名= (select 船名 from deleted) and 各证书有效期.证书名='适航证书'
DELETE FROM 各证书有效期 where 各证书有效期.船名= (select 船名 from deleted) and 各证书有效期.证书名='年度检验'
DELETE FROM 各证书有效期 where 各证书有效期.船名= (select 船名 from deleted) and 各证书有效期.证书名='中间检验'
DELETE FROM 各证书有效期 where 各证书有效期.船名= (select 船名 from deleted) and 各证书有效期.证书名='锅炉检验'
DELETE FROM 各证书有效期 where 各证书有效期.船名= (select 船名 from deleted) and 各证书有效期.证书名='特别检验'
DELETE FROM 各证书有效期 where 各证书有效期.船名= (select 船名 from deleted) and 各证书有效期.证书名='坞内检验'
DELETE FROM 各证书有效期 where 各证书有效期.船名= (select 船名 from deleted) and 各证书有效期.证书名='螺旋桨尾轴检验'
end
GO
SET QUOTED_IDENTIFIER OFF 
GO
SET ANSI_NULLS ON 
GO

--初始化数据库表
insert into 费用设置表 values('航道费','按船舶总吨计算',0,0,0,0,0,0)
GO
insert into 费用设置表 values('水运费','按载重吨数计算',0,0,0,0,0,0)
GO
insert into 系统参数表 values('提前提示天数',31)
GO
insert into 系统用户表 values('admin','d41d8cd98f00b204e9800998ecf8427e','111111','测试','0752-5357222')
GO