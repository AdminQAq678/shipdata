/*
 Navicat Premium Data Transfer

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 80020
 Source Host           : localhost:3306
 Source Schema         : shipdata

 Target Server Type    : MySQL
 Target Server Version : 80020
 File Encoding         : 65001

 Date: 23/05/2020 23:41:10
*/

ALTER DATABASE 
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;
drop database if exists shipdata;
CREATE DATABASE shipdata;
USE shipdata;
-- ----------------------------
-- Table structure for 中间检验处理历史表
-- ----------------------------
DROP TABLE IF EXISTS `中间检验处理历史表`;
CREATE TABLE `中间检验处理历史表`  (
  `序号` INT(0) NOT NULL,
  `船名` VARCHAR(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书编号` VARCHAR(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `办理日期` datetime NOT NULL,
  `办理人` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书有效期至` datetime NOT NULL,
  `业务办理情况` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 危险品证书处理历史表
-- ----------------------------
DROP TABLE IF EXISTS `危险品证书处理历史表`;
CREATE TABLE `危险品证书处理历史表`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `办理日期` datetime NOT NULL,
  `办理人` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书有效期至` datetime NOT NULL,
  `业务办理情况` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 各证书有效期
-- ----------------------------
DROP TABLE IF EXISTS `各证书有效期`;
CREATE TABLE `各证书有效期`  (
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书名` varchar(18) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书有效期至` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`船名`, `证书名`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 国籍证书处理历史表
-- ----------------------------
DROP TABLE IF EXISTS `国籍证书处理历史表`;
CREATE TABLE `国籍证书处理历史表`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `办理日期` datetime NOT NULL,
  `办理人` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书有效期至` datetime NOT NULL,
  `业务办理情况` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 坞内检验处理历史表
-- ----------------------------
DROP TABLE IF EXISTS `坞内检验处理历史表`;
CREATE TABLE `坞内检验处理历史表`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `办理日期` datetime NOT NULL,
  `办理人` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书有效期至` datetime NOT NULL,
  `业务办理情况` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 年度检验处理历史表
-- ----------------------------
DROP TABLE IF EXISTS `年度检验处理历史表`;
CREATE TABLE `年度检验处理历史表`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `办理日期` datetime NOT NULL,
  `办理人` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书有效期至` datetime NOT NULL,
  `业务办理情况` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 检修证明
-- ----------------------------
DROP TABLE IF EXISTS `检修证明`;
CREATE TABLE `检修证明`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `检修类型` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `签发时间` datetime NOT NULL,
  `检修证明编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `下次检修时间` datetime NOT NULL,
  `筏站名称` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `是否有效` varchar(4) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `检修情况说明` varchar(300) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 油污证书处理历史表
-- ----------------------------
DROP TABLE IF EXISTS `油污证书处理历史表`;
CREATE TABLE `油污证书处理历史表`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `办理日期` datetime NOT NULL,
  `办理人` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书有效期至` datetime NOT NULL,
  `业务办理情况` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 港澳航线船舶运营证
-- ----------------------------
DROP TABLE IF EXISTS `港澳航线船舶运营证`;
CREATE TABLE `港澳航线船舶运营证`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `载客定额` int(0) NULL DEFAULT NULL,
  `载货定额` decimal(18, 2) NULL DEFAULT NULL,
  `经济性质` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `船舶经营人` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `批准机关` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `批准文号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `客运航线` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `货运航线` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `发证日期` datetime NOT NULL,
  `有效日期` datetime NOT NULL,
  PRIMARY KEY (`船名`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 港澳证明处理历史表
-- ----------------------------
DROP TABLE IF EXISTS `港澳证明处理历史表`;
CREATE TABLE `港澳证明处理历史表`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `办理日期` datetime NOT NULL,
  `办理人` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书有效期至` datetime NOT NULL,
  `业务办理情况` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 特别检验处理历史表
-- ----------------------------
DROP TABLE IF EXISTS `特别检验处理历史表`;
CREATE TABLE `特别检验处理历史表`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `办理日期` datetime NOT NULL,
  `办理人` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书有效期至` datetime NOT NULL,
  `业务办理情况` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 系统参数表
-- ----------------------------
DROP TABLE IF EXISTS `系统参数表`;
CREATE TABLE `系统参数表`  (
  `序号` int(0) NOT NULL,
  `参数名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `取值` int(0) NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 系统用户表
-- ----------------------------
DROP TABLE IF EXISTS `系统用户表`;
CREATE TABLE `系统用户表`  (
  `用户ID` int(0) NOT NULL,
  `密码` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `权限` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `员工姓名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `联系电话` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`用户ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 航行港澳船舶证明书
-- ----------------------------
DROP TABLE IF EXISTS `航行港澳船舶证明书`;
CREATE TABLE `航行港澳船舶证明书`  (
  `序号` int(0) NOT NULL,
  `船舶名称` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `船员定额` int(0) NOT NULL,
  `船舶种类` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `载重吨位` decimal(18, 2) NOT NULL,
  `船籍港` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `所属单位` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `航行有效期` datetime NOT NULL,
  `批复文号` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `签发机关` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `发证日期` datetime NOT NULL,
  PRIMARY KEY (`船舶名称`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 航道费记录表
-- ----------------------------
DROP TABLE IF EXISTS `航道费记录表`;
CREATE TABLE `航道费记录表`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `航道费用` double(6, 0) NOT NULL,
  `交付日期` datetime NOT NULL,
  `费用有效期` datetime NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 船舶共有情况
-- ----------------------------
DROP TABLE IF EXISTS `船舶共有情况`;
CREATE TABLE `船舶共有情况`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `股东名` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `股份` decimal(18, 0) NULL DEFAULT NULL,
  PRIMARY KEY (`船名`, `股东名`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 船舶国籍证书
-- ----------------------------
DROP TABLE IF EXISTS `船舶国籍证书`;
CREATE TABLE `船舶国籍证书`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `曾用名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `证书编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书有效期` datetime NOT NULL,
  `取得所有权日期` datetime NOT NULL,
  `签发日期` datetime NOT NULL,
  `发证机关及其编号` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`船名`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 船舶所有权登记证书
-- ----------------------------
DROP TABLE IF EXISTS `船舶所有权登记证书`;
CREATE TABLE `船舶所有权登记证书`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `登记号码` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `初次登记号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `曾用名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `船籍港` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `原船籍港` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `船舶呼号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `IMO编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `船舶种类` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `船体材料` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `造船地点` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `建成日期` datetime NOT NULL,
  `船舶价值` double(6, 0) NULL DEFAULT NULL,
  `总长` decimal(18, 2) NOT NULL,
  `型宽` decimal(18, 2) NOT NULL,
  `型深` decimal(18, 2) NOT NULL,
  `总吨` decimal(18, 2) NOT NULL,
  `净吨` decimal(18, 2) NOT NULL,
  `主机种类` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `主机数目` int(0) NOT NULL,
  `功率` decimal(18, 2) NOT NULL,
  `推进器种类` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `推进器数目` int(0) NOT NULL,
  `船舶所有人` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `船舶所有人地址` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `法定代表人姓名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `取得所有权日期` datetime NULL DEFAULT NULL,
  `发证机关` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `发证日期` datetime NOT NULL,
  PRIMARY KEY (`船名`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 船舶最低安全配员证书
-- ----------------------------
DROP TABLE IF EXISTS `船舶最低安全配员证书`;
CREATE TABLE `船舶最低安全配员证书`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `船舶种类` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `船籍港` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `签发日期` datetime NOT NULL,
  `发证机关` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书有效期至` datetime NOT NULL,
  PRIMARY KEY (`船名`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 船舶电台执照
-- ----------------------------
DROP TABLE IF EXISTS `船舶电台执照`;
CREATE TABLE `船舶电台执照`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `呼号` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `隶属单位` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `公众通信类别` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `签发日期` datetime NOT NULL,
  `有效期至` datetime NOT NULL,
  PRIMARY KEY (`船名`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 船舶相片
-- ----------------------------
DROP TABLE IF EXISTS `船舶相片`;
CREATE TABLE `船舶相片`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `船舶相片` blob NULL,
  `相片类型` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`船名`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 船舶载重线证书
-- ----------------------------
DROP TABLE IF EXISTS `船舶载重线证书`;
CREATE TABLE `船舶载重线证书`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `船检登记号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `船长` decimal(18, 2) NULL DEFAULT NULL,
  `计算型深` decimal(18, 2) NULL DEFAULT NULL,
  `发证日期` datetime NOT NULL,
  `有效日期` datetime NOT NULL,
  PRIMARY KEY (`船名`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 船舶运载危险品证书
-- ----------------------------
DROP TABLE IF EXISTS `船舶运载危险品证书`;
CREATE TABLE `船舶运载危险品证书`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `船检登记号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `发证日期` datetime NOT NULL,
  `证书有效期` datetime NOT NULL,
  `发证机关` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `危险品种类` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`船名`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 船舶防止油污证书
-- ----------------------------
DROP TABLE IF EXISTS `船舶防止油污证书`;
CREATE TABLE `船舶防止油污证书`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `船检登记号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `船舶种类` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `建造日期` datetime NOT NULL,
  `证书有效期` datetime NOT NULL,
  `发证日期` datetime NOT NULL,
  PRIMARY KEY (`船名`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 螺旋桨尾轴检验处理历史表
-- ----------------------------
DROP TABLE IF EXISTS `螺旋桨尾轴检验处理历史表`;
CREATE TABLE `螺旋桨尾轴检验处理历史表`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `办理日期` datetime NOT NULL,
  `办理人` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书有效期至` datetime NOT NULL,
  `业务办理情况` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 货船适航证书
-- ----------------------------
DROP TABLE IF EXISTS `货船适航证书`;
CREATE TABLE `货船适航证书`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `船检登记号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书有效期` datetime NOT NULL,
  `年度检验日期` datetime NULL DEFAULT NULL,
  `中间检验日期` datetime NULL DEFAULT NULL,
  `特别检验日期` datetime NULL DEFAULT NULL,
  `坞内检验日期` datetime NULL DEFAULT NULL,
  `螺旋桨尾轴检验日期` datetime NULL DEFAULT NULL,
  `锅炉检验日期` datetime NULL DEFAULT NULL,
  `航区航线` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `发证日期` datetime NOT NULL,
  `发证单位` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `主任验船师` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`船名`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 载重线证书处理历史表
-- ----------------------------
DROP TABLE IF EXISTS `载重线证书处理历史表`;
CREATE TABLE `载重线证书处理历史表`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `办理日期` datetime NOT NULL,
  `办理人` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书有效期至` datetime NOT NULL,
  `业务办理情况` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 运营证处理历史表
-- ----------------------------
DROP TABLE IF EXISTS `运营证处理历史表`;
CREATE TABLE `运营证处理历史表`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `办理日期` datetime NOT NULL,
  `办理人` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书有效期至` datetime NOT NULL,
  `业务办理情况` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 适航证书处理历史表
-- ----------------------------
DROP TABLE IF EXISTS `适航证书处理历史表`;
CREATE TABLE `适航证书处理历史表`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `办理日期` datetime NOT NULL,
  `办理人` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书有效期至` datetime NOT NULL,
  `业务办理情况` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 配员证书处理历史表
-- ----------------------------
DROP TABLE IF EXISTS `配员证书处理历史表`;
CREATE TABLE `配员证书处理历史表`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `办理日期` datetime NOT NULL,
  `办理人` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书有效期至` datetime NOT NULL,
  `业务办理情况` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for 锅炉检验处理历史表
-- ----------------------------
DROP TABLE IF EXISTS `锅炉检验处理历史表`;
CREATE TABLE `锅炉检验处理历史表`  (
  `序号` int(0) NOT NULL,
  `船名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书编号` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `办理日期` datetime NOT NULL,
  `办理人` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `证书有效期至` datetime NOT NULL,
  `业务办理情况` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
