use uhd_whitelist;
create table log_white_list(
idx BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
rowCreateTime TIMESTAMP DEFAULT NOW(),
ProgramName text NOT NULL,
fileName text NOT NULL,
lastWriteTime DATETIME NOT NULL,
errorCode bool,
functionName text, 
returnValue bool, 
creationTime DATETIME,
fileSize BIGINT UNSIGNED,
isHidden bool
);