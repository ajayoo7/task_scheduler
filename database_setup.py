from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class TaskList(Base):
    __tablename__ = 'tasklist'

    UniqueId = Column(String(32), primary_key=True)
    Title = Column(String(250), nullable=False)
    CreatedTime = Column(String(250), nullable=False)
    CreatedDate = Column(String(250), nullable=False)
   
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'Title': self.Title,
            'UniqueId': self.UniqueId,
            'CreatedTime': self.CreatedTime,
            'CreatedDate': self.CreatedDate,
        }


class Scheduler(Base):
    __tablename__ = 'scheduler'

    UniqueKey = Column(String(16), primary_key=True)
    TaskUniqueId = Column(String(32), ForeignKey('tasklist.UniqueId'))
    ScheduledTime =Column(String(250), nullable=False)
    Status= Column(Integer, nullable=False)
    tasklist = relationship(TaskList)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'UniqueKey': self.UniqueKey,
            'TaskUniqueId': self.TaskUniqueId,
            'ScheduledTime': self.ScheduledTime,
            'Status': self.Status,
        }

class BasicCronInsight(Base):
    __tablename__ = 'basiccroninsight'

    UniqueId = Column(String(32), primary_key=True)
    Compleated= Column(Integer)
    ExecutionTime = Column(String(250),nullable=False)
    CronDate = Column (String(250),nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'UniqueId': self.UniqueId,
            'ExecutionTime': self.ExecutionTime,
            'Compleated': self.Compleated,
            'CronDate': self.CronDate,
        }


class TrackingKey(Base):
    __tablename__ = 'trackingkey'

    UniqueId = Column(String(32), primary_key=True)
    TrackKey = Column(String(5), nullable= False)
    TaskUniqueId = Column(String(32), ForeignKey('tasklist.UniqueId'))
    Time = Column(String(250), nullable= False)
    tasklist = relationship(TaskList)



    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'UniqueId': self.UniqueId,
            'TrackingKey': self.TrackKey,
            'TaskUniqueId': self.TaskUniqueId,
            'CreatedTime': self.Time
        }


engine = create_engine('sqlite:///taskinsight.db')


Base.metadata.create_all(engine)