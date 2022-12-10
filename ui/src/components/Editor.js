import React, { useState, useMemo } from 'react';
import { createEditor } from 'slate';
import { Slate, Editable, withReact } from 'slate-react';


  const Editor = ({ document, onChange }) => {
    const editor = useMemo(() => withReact(createEditor()), []);
    
    return (
      <Slate editor={editor} value={document}>
        <Editable />
      </Slate>
    );
  }

  export default Editor;