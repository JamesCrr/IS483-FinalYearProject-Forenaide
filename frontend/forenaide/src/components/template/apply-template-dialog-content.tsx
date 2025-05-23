import React, { SetStateAction, useEffect, useState } from "react";
import {
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
  DialogFooter,
  DialogClose,
} from "../ui/dialog";
import { Button } from "../ui/button";
import { Label } from "../ui/label";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "../ui/select";
import { z } from "zod";
import { useToast } from "@/hooks/use-toast";
import { SchemaField } from "@/types/schema-field";
import { useSchemaFieldStore } from "@/hooks/use-schema-field-store";
import { TemplateResponseType } from "@/types/template-field";
import { apiEndpoint } from "@/lib/api";

export function ApplyTemplateDialogContent() {
  const { toast } = useToast();
  const { concatIntoConfig } = useSchemaFieldStore();
  const [templates, setTemplates] = useState<TemplateResponseType[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [selectedFields, setSelectedFields] = useState<SchemaField[]>([]);
  useEffect(() => {
    const getTemplates = async () => {
      setIsLoading(true);
      const get_template_url = `${apiEndpoint}/templates`;

      try {
        const response = await fetch(get_template_url);
        if (!response.ok) {
          throw new Error(`Error: ${response.status} ${response.statusText}`);
        }
        const data = await response.json();
        setTemplates(data);
      } catch (error) {
        console.error("Error retrieving templates:", error);
        // Assuming toast is available in this context
        toast({
          title: "Error",
          description: "Failed to retrieve templates",
          variant: "destructive",
        });
      } finally {
        setIsLoading(false);
      }
    };
    getTemplates();
  }, []);

  const onConfirm = () => {
    console.log(selectedFields);
    concatIntoConfig(selectedFields);
  };
  return (
    <DialogContent className="sm:max-w-[425px]">
      <DialogHeader>
        <DialogTitle>Use Existing Template</DialogTitle>
        <DialogDescription>
          Use a previously saved template with pre-defined schema fields
        </DialogDescription>
      </DialogHeader>
      <div className="grid gap-4">
        <Select
          disabled={isLoading}
          onValueChange={(value) => {
            const selectedTemplate = templates.filter(
              (template) => template.id === value
            );
            const {
              schema: { fields },
            } = selectedTemplate[0];
            setSelectedFields(fields as SchemaField[]);
          }}
          aria-hidden={false} // Ensure aria-hidden is not set to true
        >
          <SelectTrigger className="w-full">
            <SelectValue placeholder="Choose Existing Template" />
          </SelectTrigger>
          <SelectContent>
            {templates.map((template) => {
              return (
                <SelectItem value={template.id} key={template.id}>
                  {template.name}
                </SelectItem>
              );
            })}
          </SelectContent>
        </Select>
      </div>
      <DialogFooter>
        <DialogClose>
          <Button type="button" onClick={onConfirm}>
            Confirm
          </Button>
        </DialogClose>
      </DialogFooter>
    </DialogContent>
  );
}
