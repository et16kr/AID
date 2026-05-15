---
title: "How to manage Spring+iBatis transaction"
page_id: "16876194"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876194"
updated_at: "2021-04-05T09:51:42.000+0900"
version: 3
ancestors: ["Home", "07. Development and API"]
labels: []
---

# How to manage Spring+iBatis transaction
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876194
Updated: 2021-04-05T09:51:42.000+0900

**- [Overview](#HowtomanageSpring+iBatistransaction-Overview) - [How to manage](#HowtomanageSpring+iBatistransaction-Howtomanage) - [Detailed description](#HowtomanageSpring+iBatistransaction-Detaileddescription) - [Common application](#HowtomanageSpring+iBatistransaction-Commonapplication) - [1-1. When using DataSourceTransactionManager directly](#HowtomanageSpring+iBatistransaction-1-1.WhenusingDataSourceTransactionManagerdirectly) - [1-2. When to use TransactionTemplate](#HowtomanageSpring+iBatistransaction-1-2.WhentouseTransactionTemplate) - [2-1. Method using <tx:advice> tag](#HowtomanageSpring+iBatistransaction-2-1.Methodusing<tx:advice>tag) - [2-2. Method using TransactionProxyFactoryBean tag](#HowtomanageSpring+iBatistransaction-2-2.MethodusingTransactionProxyFactoryBeantag) - [2-3 Method using the @Transactional annotation](#HowtomanageSpring+iBatistransaction-2-3Methodusingthe@Transactionalannotation) - [Reference](#HowtomanageSpring+iBatistransaction-Reference) - [Sample code](#HowtomanageSpring+iBatistransaction-Samplecode)**

# Overview

---

This document describes how to manage Spring+iBatis transactions.

# How to manage

---

**1. Bean Managed Transaction (BMT), explicit transaction management (how to consider transaction processing in the source)**

1-1 When directly using DataSourceTransactionManager

1-2 When using TransactionTemplate

**2. CMT (Container Managed Transaction), declarative transaction management (using a configuration file and reducing consideration for transaction processing in the source)**

2-1 Method using <tx:advice> tag

2-2. Method using TransactionProxyFactoryBean tag

2-3 Method using the @Transactional annotation

# Detailed description

---

## Common application

---

**applicationContext.xml**

```
<bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource" >
   <property name="driverClassName"><value>Altibase.jdbc.driver.AltibaseDriver</value></property>
   <property name="url"><value>jdbc:Altibase://192.168.1.82:20300/mydb</value></property>
   <property name="username"><value>sys</value></property>
   <property name="password"><value>manager</value></property>
   <property name="maxActive"><value>20</value></property>
   <property name="maxIdle"><value>30000</value></property>
   <property name="maxWait"><value>100</value></property>
  </bean>

  <bean id="transactionManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
   <property name="dataSource"><ref local="dataSource"/></property>
  </bean>
```

## 1-1. When using DataSourceTransactionManager directly

---

- Configuration file: There is no additional configuration.
- Commit and rollback are processed directly on the source.
  SetAutoCommit(false) must be called in order to process as a transaction.
  Note that setAutoCommit(false) must be called when selecting blobs.

## 1-2. When to use TransactionTemplate

---

- Configuration file

  ```
    <bean id="transactionTemplate" class="org.springframework.transaction.support.TransactionTemplate">
     <property name="transactionManager"><ref local="transactionManager"/></property>
    </bean>

    <bean id="xxxService" class="…">
     <property name="transactionTemplate"><ref local=" transactionTemplate"/></property>
    </bean>
  ```
- The user must use functions such as transactionTemplate.execute() and doInTransaction() on the source.
- Note that when selecting blobs, Oracle did not process transactions, but when using Altibase, the user must use functions such as transactionTemplate.execute() and doInTransaction() on the source to process transactions.

## 2-1. Method using <tx:advice> tag

---

- Configuration file

  ```
  <bean id="sqlMapClient" class="org.springframework.orm.ibatis.SqlMapClientFactoryBean">
       <property name="configLocation"><value>sqlmap.xml</value></property>
       <property name="dataSource"><ref bean="dataSource" /></property>
       <property name="lobHandler"><ref bean="defaultLobHandler"/></property>
       <property name="transactionConfigProperties">
          <props>
             <prop key="DefaultAutoCommit">false</prop>
             <prop key="SetAutoCommitAllowed">true</prop>
          </props>
       </property>
  </bean>
  <tx:advice id="txAdvice" transaction-manager="transactionManager">
      <tx:attributes>
        <!-- all methods starting with 'get' are read-only -->
        <tx:method name="get*" read-only="true" rollback-for="Exception"/>
        <!-- other methods use the default transaction settings (see below) -->
        <tx:method name="*" propagation=”REQUIRED”/>
      </tx:attributes>
  </tx:advice>
  ```
- There is no need for transaction-related code on the source.

## 2-2. Method using TransactionProxyFactoryBean tag

---

- Configuration file

  ```
   <bean id="sqlMapClient" class="org.springframework.orm.ibatis.SqlMapClientFactoryBean">
       <property name="configLocation"><value>sqlmap.xml</value></property>
       <property name="dataSource"><ref bean="dataSource" /></property>
       <property name="lobHandler"><ref bean="defaultLobHandler"/></property>
       <property name="transactionConfigProperties">
          <props>
             <prop key="DefaultAutoCommit">false</prop>
             <prop key="SetAutoCommitAllowed">true</prop>
          </props>
       </property>
   </bean>
   <bean id="txProxyTemplate" abstract="true" class="org.springframework.transaction.interceptor.TransactionProxyFactoryBean">
     <property name="transactionManager">
      <ref local="transactionManager"></ref>
     </property>
     <property name="transactionAttributes">
      <props>
       <prop key="insert*">PROPAGATION_REQUIRED</prop>
       <prop key="update*">PROPAGATION_REQUIRED</prop>
       <prop key="delete*">PROPAGATION_REQUIRED</prop>
       <prop key="save*">PROPAGATION_REQUIRED</prop>
       <prop key="*">PROPAGATION_SUPPORTS</prop>
      </props>
     </property>
   </bean>
  ```
- There is no need for transaction-related code on the source.

## 2-3 Method using the @Transactional annotation

---

- Configuration

  ```
  <bean id="sqlMapClient" class="org.springframework.orm.ibatis.SqlMapClientFactoryBean">
       <property name="configLocation"><value>sqlmap.xml</value></property>
       <property name="dataSource"><ref bean="dataSource" /></property>
       <property name="lobHandler"><ref bean="defaultLobHandler"/></property>
       <property name="transactionConfigProperties">
          <props>
             <prop key="DefaultAutoCommit">false</prop>
             <prop key="SetAutoCommitAllowed">true</prop>
          </props>
       </property>
    </bean>
    <tx:annotation-driven transaction-manager="transactionManager"/>
  ```
- Classes that require transactions on the source require @Transactional(propagation=Propagation.REQUIRED) notation.

# Reference

---

- If AltibaseClobStringTypeHandler is applied guided by the standard framework, an error may occur when CLOB is 0 byte.
  In this case, the user can check that it is normally searched by adding annotations without using TypeHandler.

# Sample code

---

Sample code for handling LOB data.

- [LobSpringIbatisSample.zip](https://docs.altibase.com/download/attachments/9109742/LobSpringIbatisSample.zip?version=1&modificationDate=1447388295000&api=v2)
