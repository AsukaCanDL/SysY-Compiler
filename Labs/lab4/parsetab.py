
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CompUnitAND Assign Break COMMENT Comma Const Continue DECIMAL Div Else Eq Ge Gt HEXADECIMAL IDENT If Int LBrace LPar Le Lt Main Minus Mod Mult NotEq OCTAL OR Plus RBrace RESERVED RPar Return Semicolon SysFunc While CompUnit : FuncDef  FuncDef : FuncType Main LPar RPar Block FuncType : Int  Block : LBrace AddBlock RBrace  AddBlock : BlockItem \n                 | BlockItem AddBlock BlockItem : Decl \n                  | Stmt  Decl : ConstDecl \n             | VarDecl ConstDecl : Const BType AddConstDef Semicolon  AddConstDef : ConstDef Comma AddConstDef\n                    | ConstDef  ConstDef : IDENT Assign ConstInitVal  BType : Int ConstInitVal : AddExp  VarDecl : BType AddVarDef Semicolon  AddVarDef : VarDef Comma AddVarDef\n                  | VarDef  VarDef  : IDENT\n                | IDENT Assign InitVal  InitVal : Exp  Stmt : Semicolon\n             | Block\n             | Exp Semicolon \n             | Return Exp Semicolon \n             | LVal Assign Exp Semicolon\n             | If LPar Cond RPar Stmt \n             | If LPar Cond RPar Stmt Else Stmt  Cond : LOrExp  LOrExp : LAndExp\n               | LOrExp OR LAndExp  LAndExp : EqExp\n                | LAndExp AND EqExp  EqExp : RelExp\n              | EqExp Eq RelExp \n              | EqExp NotEq RelExp  RelExp : AddExp\n               | RelExp Lt AddExp\n               | RelExp Gt AddExp\n               | RelExp Le AddExp\n               | RelExp Ge AddExp  LVal : IDENT  Exp : AddExp  AddExp : MulExp \n               | AddExp Plus MulExp\n               | AddExp Minus MulExp  MulExp : UnaryExp \n               | MulExp Div UnaryExp\n               | MulExp Mult UnaryExp\n               | MulExp Mod UnaryExp UnaryExp : PrimaryExp \n                 | Plus UnaryExp\n                 | Minus UnaryExp \n                 | SysFunc LPar RPar\n                 | SysFunc LPar FuncRParams RPar  FuncRParams : Exp Exps\n                    | Exp  Exps : Comma Exp  PrimaryExp : LPar Exp RPar \n                   | Number \n                   | LVal  Number  : DECIMAL \n                | OCTAL \n                | HEXADECIMAL '
    
_lr_action_items = {'Int':([0,9,11,12,13,14,15,16,17,23,38,40,58,70,81,91,100,114,],[4,27,27,-7,-8,-9,-10,-23,-24,27,-4,-25,-26,-17,-27,-11,-28,-29,]),'$end':([1,2,8,38,],[0,-1,-2,-4,]),'Main':([3,4,],[5,-3,]),'LPar':([5,9,11,12,13,14,15,16,17,19,21,22,29,30,33,38,40,43,44,50,51,52,53,54,57,58,70,72,81,82,83,84,85,86,87,88,89,90,91,93,99,100,113,114,],[6,22,22,-7,-8,-9,-10,-23,-24,22,44,22,22,22,57,-4,-25,22,22,22,22,22,22,22,22,-26,-17,22,-27,22,22,22,22,22,22,22,22,22,-11,22,22,-28,22,-29,]),'RPar':([6,25,26,28,31,32,34,35,36,37,42,45,55,56,57,60,61,62,63,64,65,66,73,74,75,76,77,78,79,80,97,98,101,102,103,104,105,106,107,108,112,],[7,-44,-43,-45,-48,-52,-61,-63,-64,-65,-62,66,-53,-54,78,82,-30,-31,-33,-35,-38,-60,-46,-47,-49,-50,-51,-55,97,-58,-56,-57,-32,-34,-36,-37,-39,-40,-41,-42,-59,]),'LBrace':([7,9,11,12,13,14,15,16,17,38,40,58,70,81,82,91,100,113,114,],[9,9,9,-7,-8,-9,-10,-23,-24,-4,-25,-26,-17,-27,9,-11,-28,9,-29,]),'Semicolon':([9,11,12,13,14,15,16,17,18,20,25,26,28,31,32,34,35,36,37,38,40,41,42,47,48,49,55,56,58,59,66,67,68,70,73,74,75,76,77,78,81,82,91,94,95,96,97,100,109,110,111,113,114,],[16,16,-7,-8,-9,-10,-23,-24,40,-62,-44,-43,-45,-48,-52,-61,-63,-64,-65,-4,-25,58,-62,70,-19,-20,-53,-54,-26,81,-60,91,-13,-17,-46,-47,-49,-50,-51,-55,-27,16,-11,-18,-21,-22,-56,-28,-12,-14,-16,16,-29,]),'Return':([9,11,12,13,14,15,16,17,38,40,58,70,81,82,91,100,113,114,],[19,19,-7,-8,-9,-10,-23,-24,-4,-25,-26,-17,-27,19,-11,-28,19,-29,]),'If':([9,11,12,13,14,15,16,17,38,40,58,70,81,82,91,100,113,114,],[21,21,-7,-8,-9,-10,-23,-24,-4,-25,-26,-17,-27,21,-11,-28,21,-29,]),'Const':([9,11,12,13,14,15,16,17,38,40,58,70,81,91,100,114,],[23,23,-7,-8,-9,-10,-23,-24,-4,-25,-26,-17,-27,-11,-28,-29,]),'IDENT':([9,11,12,13,14,15,16,17,19,22,24,27,29,30,38,40,43,44,46,50,51,52,53,54,57,58,70,71,72,81,82,83,84,85,86,87,88,89,90,91,92,93,99,100,113,114,],[26,26,-7,-8,-9,-10,-23,-24,26,26,49,-15,26,26,-4,-25,26,26,69,26,26,26,26,26,26,-26,-17,49,26,-27,26,26,26,26,26,26,26,26,26,-11,69,26,26,-28,26,-29,]),'Plus':([9,11,12,13,14,15,16,17,19,20,22,25,26,28,29,30,31,32,34,35,36,37,38,40,42,43,44,50,51,52,53,54,55,56,57,58,65,66,70,72,73,74,75,76,77,78,81,82,83,84,85,86,87,88,89,90,91,93,97,99,100,105,106,107,108,111,113,114,],[29,29,-7,-8,-9,-10,-23,-24,29,-62,29,50,-43,-45,29,29,-48,-52,-61,-63,-64,-65,-4,-25,-62,29,29,29,29,29,29,29,-53,-54,29,-26,50,-60,-17,29,-46,-47,-49,-50,-51,-55,-27,29,29,29,29,29,29,29,29,29,-11,29,-56,29,-28,50,50,50,50,50,29,-29,]),'Minus':([9,11,12,13,14,15,16,17,19,20,22,25,26,28,29,30,31,32,34,35,36,37,38,40,42,43,44,50,51,52,53,54,55,56,57,58,65,66,70,72,73,74,75,76,77,78,81,82,83,84,85,86,87,88,89,90,91,93,97,99,100,105,106,107,108,111,113,114,],[30,30,-7,-8,-9,-10,-23,-24,30,-62,30,51,-43,-45,30,30,-48,-52,-61,-63,-64,-65,-4,-25,-62,30,30,30,30,30,30,30,-53,-54,30,-26,51,-60,-17,30,-46,-47,-49,-50,-51,-55,-27,30,30,30,30,30,30,30,30,30,-11,30,-56,30,-28,51,51,51,51,51,30,-29,]),'SysFunc':([9,11,12,13,14,15,16,17,19,22,29,30,38,40,43,44,50,51,52,53,54,57,58,70,72,81,82,83,84,85,86,87,88,89,90,91,93,99,100,113,114,],[33,33,-7,-8,-9,-10,-23,-24,33,33,33,33,-4,-25,33,33,33,33,33,33,33,33,-26,-17,33,-27,33,33,33,33,33,33,33,33,33,-11,33,33,-28,33,-29,]),'DECIMAL':([9,11,12,13,14,15,16,17,19,22,29,30,38,40,43,44,50,51,52,53,54,57,58,70,72,81,82,83,84,85,86,87,88,89,90,91,93,99,100,113,114,],[35,35,-7,-8,-9,-10,-23,-24,35,35,35,35,-4,-25,35,35,35,35,35,35,35,35,-26,-17,35,-27,35,35,35,35,35,35,35,35,35,-11,35,35,-28,35,-29,]),'OCTAL':([9,11,12,13,14,15,16,17,19,22,29,30,38,40,43,44,50,51,52,53,54,57,58,70,72,81,82,83,84,85,86,87,88,89,90,91,93,99,100,113,114,],[36,36,-7,-8,-9,-10,-23,-24,36,36,36,36,-4,-25,36,36,36,36,36,36,36,36,-26,-17,36,-27,36,36,36,36,36,36,36,36,36,-11,36,36,-28,36,-29,]),'HEXADECIMAL':([9,11,12,13,14,15,16,17,19,22,29,30,38,40,43,44,50,51,52,53,54,57,58,70,72,81,82,83,84,85,86,87,88,89,90,91,93,99,100,113,114,],[37,37,-7,-8,-9,-10,-23,-24,37,37,37,37,-4,-25,37,37,37,37,37,37,37,37,-26,-17,37,-27,37,37,37,37,37,37,37,37,37,-11,37,37,-28,37,-29,]),'RBrace':([10,11,12,13,14,15,16,17,38,39,40,58,70,81,91,100,114,],[38,-5,-7,-8,-9,-10,-23,-24,-4,-6,-25,-26,-17,-27,-11,-28,-29,]),'Else':([16,17,38,40,58,81,100,114,],[-23,-24,-4,-25,-26,-27,113,-29,]),'Assign':([20,26,49,69,],[43,-43,72,93,]),'Div':([20,26,28,31,32,34,35,36,37,42,55,56,66,73,74,75,76,77,78,97,],[-62,-43,52,-48,-52,-61,-63,-64,-65,-62,-53,-54,-60,52,52,-49,-50,-51,-55,-56,]),'Mult':([20,26,28,31,32,34,35,36,37,42,55,56,66,73,74,75,76,77,78,97,],[-62,-43,53,-48,-52,-61,-63,-64,-65,-62,-53,-54,-60,53,53,-49,-50,-51,-55,-56,]),'Mod':([20,26,28,31,32,34,35,36,37,42,55,56,66,73,74,75,76,77,78,97,],[-62,-43,54,-48,-52,-61,-63,-64,-65,-62,-53,-54,-60,54,54,-49,-50,-51,-55,-56,]),'Comma':([25,26,28,31,32,34,35,36,37,42,48,49,55,56,66,68,73,74,75,76,77,78,80,95,96,97,110,111,],[-44,-43,-45,-48,-52,-61,-63,-64,-65,-62,71,-20,-53,-54,-60,92,-46,-47,-49,-50,-51,-55,99,-21,-22,-56,-14,-16,]),'Lt':([26,28,31,32,34,35,36,37,42,55,56,64,65,66,73,74,75,76,77,78,97,103,104,105,106,107,108,],[-43,-45,-48,-52,-61,-63,-64,-65,-62,-53,-54,87,-38,-60,-46,-47,-49,-50,-51,-55,-56,87,87,-39,-40,-41,-42,]),'Gt':([26,28,31,32,34,35,36,37,42,55,56,64,65,66,73,74,75,76,77,78,97,103,104,105,106,107,108,],[-43,-45,-48,-52,-61,-63,-64,-65,-62,-53,-54,88,-38,-60,-46,-47,-49,-50,-51,-55,-56,88,88,-39,-40,-41,-42,]),'Le':([26,28,31,32,34,35,36,37,42,55,56,64,65,66,73,74,75,76,77,78,97,103,104,105,106,107,108,],[-43,-45,-48,-52,-61,-63,-64,-65,-62,-53,-54,89,-38,-60,-46,-47,-49,-50,-51,-55,-56,89,89,-39,-40,-41,-42,]),'Ge':([26,28,31,32,34,35,36,37,42,55,56,64,65,66,73,74,75,76,77,78,97,103,104,105,106,107,108,],[-43,-45,-48,-52,-61,-63,-64,-65,-62,-53,-54,90,-38,-60,-46,-47,-49,-50,-51,-55,-56,90,90,-39,-40,-41,-42,]),'Eq':([26,28,31,32,34,35,36,37,42,55,56,63,64,65,66,73,74,75,76,77,78,97,102,103,104,105,106,107,108,],[-43,-45,-48,-52,-61,-63,-64,-65,-62,-53,-54,85,-35,-38,-60,-46,-47,-49,-50,-51,-55,-56,85,-36,-37,-39,-40,-41,-42,]),'NotEq':([26,28,31,32,34,35,36,37,42,55,56,63,64,65,66,73,74,75,76,77,78,97,102,103,104,105,106,107,108,],[-43,-45,-48,-52,-61,-63,-64,-65,-62,-53,-54,86,-35,-38,-60,-46,-47,-49,-50,-51,-55,-56,86,-36,-37,-39,-40,-41,-42,]),'AND':([26,28,31,32,34,35,36,37,42,55,56,62,63,64,65,66,73,74,75,76,77,78,97,101,102,103,104,105,106,107,108,],[-43,-45,-48,-52,-61,-63,-64,-65,-62,-53,-54,84,-33,-35,-38,-60,-46,-47,-49,-50,-51,-55,-56,84,-34,-36,-37,-39,-40,-41,-42,]),'OR':([26,28,31,32,34,35,36,37,42,55,56,61,62,63,64,65,66,73,74,75,76,77,78,97,101,102,103,104,105,106,107,108,],[-43,-45,-48,-52,-61,-63,-64,-65,-62,-53,-54,83,-31,-33,-35,-38,-60,-46,-47,-49,-50,-51,-55,-56,-32,-34,-36,-37,-39,-40,-41,-42,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'CompUnit':([0,],[1,]),'FuncDef':([0,],[2,]),'FuncType':([0,],[3,]),'Block':([7,9,11,82,113,],[8,17,17,17,17,]),'AddBlock':([9,11,],[10,39,]),'BlockItem':([9,11,],[11,11,]),'Decl':([9,11,],[12,12,]),'Stmt':([9,11,82,113,],[13,13,100,114,]),'ConstDecl':([9,11,],[14,14,]),'VarDecl':([9,11,],[15,15,]),'Exp':([9,11,19,22,43,57,72,82,99,113,],[18,18,41,45,59,80,96,18,112,18,]),'LVal':([9,11,19,22,29,30,43,44,50,51,52,53,54,57,72,82,83,84,85,86,87,88,89,90,93,99,113,],[20,20,42,42,42,42,42,42,42,42,42,42,42,42,42,20,42,42,42,42,42,42,42,42,42,42,20,]),'BType':([9,11,23,],[24,24,46,]),'AddExp':([9,11,19,22,43,44,57,72,82,83,84,85,86,87,88,89,90,93,99,113,],[25,25,25,25,25,65,25,25,25,65,65,65,65,105,106,107,108,111,25,25,]),'MulExp':([9,11,19,22,43,44,50,51,57,72,82,83,84,85,86,87,88,89,90,93,99,113,],[28,28,28,28,28,28,73,74,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'UnaryExp':([9,11,19,22,29,30,43,44,50,51,52,53,54,57,72,82,83,84,85,86,87,88,89,90,93,99,113,],[31,31,31,31,55,56,31,31,31,31,75,76,77,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'PrimaryExp':([9,11,19,22,29,30,43,44,50,51,52,53,54,57,72,82,83,84,85,86,87,88,89,90,93,99,113,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'Number':([9,11,19,22,29,30,43,44,50,51,52,53,54,57,72,82,83,84,85,86,87,88,89,90,93,99,113,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'AddVarDef':([24,71,],[47,94,]),'VarDef':([24,71,],[48,48,]),'Cond':([44,],[60,]),'LOrExp':([44,],[61,]),'LAndExp':([44,83,],[62,101,]),'EqExp':([44,83,84,],[63,63,102,]),'RelExp':([44,83,84,85,86,],[64,64,64,103,104,]),'AddConstDef':([46,92,],[67,109,]),'ConstDef':([46,92,],[68,68,]),'FuncRParams':([57,],[79,]),'InitVal':([72,],[95,]),'Exps':([80,],[98,]),'ConstInitVal':([93,],[110,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> CompUnit","S'",1,None,None,None),
  ('CompUnit -> FuncDef','CompUnit',1,'p_CompUnit','parser_modules.py',8),
  ('FuncDef -> FuncType Main LPar RPar Block','FuncDef',5,'p_FuncDef','parser_modules.py',12),
  ('FuncType -> Int','FuncType',1,'p_FuncType','parser_modules.py',16),
  ('Block -> LBrace AddBlock RBrace','Block',3,'p_Block','parser_modules.py',20),
  ('AddBlock -> BlockItem','AddBlock',1,'p_AddBlock','parser_modules.py',24),
  ('AddBlock -> BlockItem AddBlock','AddBlock',2,'p_AddBlock','parser_modules.py',25),
  ('BlockItem -> Decl','BlockItem',1,'p_BlockItem','parser_modules.py',32),
  ('BlockItem -> Stmt','BlockItem',1,'p_BlockItem','parser_modules.py',33),
  ('Decl -> ConstDecl','Decl',1,'p_Decl','parser_modules.py',37),
  ('Decl -> VarDecl','Decl',1,'p_Decl','parser_modules.py',38),
  ('ConstDecl -> Const BType AddConstDef Semicolon','ConstDecl',4,'p_ConstDecl','parser_modules.py',42),
  ('AddConstDef -> ConstDef Comma AddConstDef','AddConstDef',3,'p_AddConstDef','parser_modules.py',46),
  ('AddConstDef -> ConstDef','AddConstDef',1,'p_AddConstDef','parser_modules.py',47),
  ('ConstDef -> IDENT Assign ConstInitVal','ConstDef',3,'p_ConstDef','parser_modules.py',54),
  ('BType -> Int','BType',1,'p_BType','parser_modules.py',58),
  ('ConstInitVal -> AddExp','ConstInitVal',1,'p_ConstInitVal','parser_modules.py',62),
  ('VarDecl -> BType AddVarDef Semicolon','VarDecl',3,'p_VarDecl','parser_modules.py',70),
  ('AddVarDef -> VarDef Comma AddVarDef','AddVarDef',3,'p_AddVarDef','parser_modules.py',74),
  ('AddVarDef -> VarDef','AddVarDef',1,'p_AddVarDef','parser_modules.py',75),
  ('VarDef -> IDENT','VarDef',1,'p_VarDef','parser_modules.py',82),
  ('VarDef -> IDENT Assign InitVal','VarDef',3,'p_VarDef','parser_modules.py',83),
  ('InitVal -> Exp','InitVal',1,'p_InitVal','parser_modules.py',90),
  ('Stmt -> Semicolon','Stmt',1,'p_Stmt','parser_modules.py',94),
  ('Stmt -> Block','Stmt',1,'p_Stmt','parser_modules.py',95),
  ('Stmt -> Exp Semicolon','Stmt',2,'p_Stmt','parser_modules.py',96),
  ('Stmt -> Return Exp Semicolon','Stmt',3,'p_Stmt','parser_modules.py',97),
  ('Stmt -> LVal Assign Exp Semicolon','Stmt',4,'p_Stmt','parser_modules.py',98),
  ('Stmt -> If LPar Cond RPar Stmt','Stmt',5,'p_Stmt','parser_modules.py',99),
  ('Stmt -> If LPar Cond RPar Stmt Else Stmt','Stmt',7,'p_Stmt','parser_modules.py',100),
  ('Cond -> LOrExp','Cond',1,'p_Cond','parser_modules.py',115),
  ('LOrExp -> LAndExp','LOrExp',1,'p_LOrExp','parser_modules.py',119),
  ('LOrExp -> LOrExp OR LAndExp','LOrExp',3,'p_LOrExp','parser_modules.py',120),
  ('LAndExp -> EqExp','LAndExp',1,'p_LAndExp','parser_modules.py',127),
  ('LAndExp -> LAndExp AND EqExp','LAndExp',3,'p_LAndExp','parser_modules.py',128),
  ('EqExp -> RelExp','EqExp',1,'p_EqExp','parser_modules.py',135),
  ('EqExp -> EqExp Eq RelExp','EqExp',3,'p_EqExp','parser_modules.py',136),
  ('EqExp -> EqExp NotEq RelExp','EqExp',3,'p_EqExp','parser_modules.py',137),
  ('RelExp -> AddExp','RelExp',1,'p_RelExp','parser_modules.py',144),
  ('RelExp -> RelExp Lt AddExp','RelExp',3,'p_RelExp','parser_modules.py',145),
  ('RelExp -> RelExp Gt AddExp','RelExp',3,'p_RelExp','parser_modules.py',146),
  ('RelExp -> RelExp Le AddExp','RelExp',3,'p_RelExp','parser_modules.py',147),
  ('RelExp -> RelExp Ge AddExp','RelExp',3,'p_RelExp','parser_modules.py',148),
  ('LVal -> IDENT','LVal',1,'p_LVal','parser_modules.py',155),
  ('Exp -> AddExp','Exp',1,'p_Exp','parser_modules.py',159),
  ('AddExp -> MulExp','AddExp',1,'p_AddExp','parser_modules.py',163),
  ('AddExp -> AddExp Plus MulExp','AddExp',3,'p_AddExp','parser_modules.py',164),
  ('AddExp -> AddExp Minus MulExp','AddExp',3,'p_AddExp','parser_modules.py',165),
  ('MulExp -> UnaryExp','MulExp',1,'p_MulExp','parser_modules.py',172),
  ('MulExp -> MulExp Div UnaryExp','MulExp',3,'p_MulExp','parser_modules.py',173),
  ('MulExp -> MulExp Mult UnaryExp','MulExp',3,'p_MulExp','parser_modules.py',174),
  ('MulExp -> MulExp Mod UnaryExp','MulExp',3,'p_MulExp','parser_modules.py',175),
  ('UnaryExp -> PrimaryExp','UnaryExp',1,'p_UnaryExp','parser_modules.py',184),
  ('UnaryExp -> Plus UnaryExp','UnaryExp',2,'p_UnaryExp','parser_modules.py',185),
  ('UnaryExp -> Minus UnaryExp','UnaryExp',2,'p_UnaryExp','parser_modules.py',186),
  ('UnaryExp -> SysFunc LPar RPar','UnaryExp',3,'p_UnaryExp','parser_modules.py',187),
  ('UnaryExp -> SysFunc LPar FuncRParams RPar','UnaryExp',4,'p_UnaryExp','parser_modules.py',188),
  ('FuncRParams -> Exp Exps','FuncRParams',2,'p_FuncRParams','parser_modules.py',199),
  ('FuncRParams -> Exp','FuncRParams',1,'p_FuncRParams','parser_modules.py',200),
  ('Exps -> Comma Exp','Exps',2,'p_Exps','parser_modules.py',207),
  ('PrimaryExp -> LPar Exp RPar','PrimaryExp',3,'p_PrimaryExp','parser_modules.py',212),
  ('PrimaryExp -> Number','PrimaryExp',1,'p_PrimaryExp','parser_modules.py',213),
  ('PrimaryExp -> LVal','PrimaryExp',1,'p_PrimaryExp','parser_modules.py',214),
  ('Number -> DECIMAL','Number',1,'p_Number','parser_modules.py',221),
  ('Number -> OCTAL','Number',1,'p_Number','parser_modules.py',222),
  ('Number -> HEXADECIMAL','Number',1,'p_Number','parser_modules.py',223),
]
