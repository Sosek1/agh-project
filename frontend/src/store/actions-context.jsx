import React, { useState, useContext } from "react";

export const ActionsContext = React.createContext();

export const useActions = () => {
  return useContext(ActionsContext);
};

export const ActionsContextProvider = (props) => {
  const [deleteAction, setDeleteAction] = useState(false);
  const [editAction, setEditAction] = useState(false);

  const deleteActionHandler = (value) => {
    setDeleteAction(value);
  };

  const editActionHandler = (value) => {
    setDeleteAction(value);
  };

  return (
    <ActionsContext.Provider
      value={{
        deleteAction,
        editAction,
        onDelete: deleteActionHandler,
        onEdit: editActionHandler,
      }}
    >
      {props.children}
    </ActionsContext.Provider>
  );
};
